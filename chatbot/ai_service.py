import requests
import json
from django.conf import settings

def get_chatbot_response(user_question):
    """
    Get educational response from OpenAI API using a direct HTTP request.
    """
    api_key = settings.OPENAI_API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful educational tutor for children aged 3-10. Provide simple, encouraging, and educational responses."},
            {"role": "user", "content": user_question}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }
    
    try:
        # Make the request, explicitly disabling proxies
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            data=json.dumps(data),
            proxies={}  # This will bypass any system-level proxy settings
        )
        
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        result = response.json()
        return result['choices'][0]['message']['content']
        
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request error: {e}")
        return "I'm sorry, I'm having trouble connecting to the AI service right now. Please try again later!"
    except (KeyError, IndexError) as e:
        print(f"Error parsing OpenAI response: {e}")
        return "I'm sorry, I received an unexpected response from the AI service. Please try again."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "I'm sorry, I'm having trouble right now. Please try asking your question again later!"