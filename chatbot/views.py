from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ChatbotSession
from .ai_service import get_chatbot_response

@login_required
def chat_view(request):
    if request.method == 'POST':
        user_question = request.POST.get('question')
        if user_question:
            # Get response from AI service
            ai_response = get_chatbot_response(user_question)
            
            # Save the interaction
            ChatbotSession.objects.create(
                user=request.user,
                question=user_question,
                response=ai_response
            )
            
            return JsonResponse({'response': ai_response})
        return JsonResponse({'error': 'No question provided'}, status=400)
    
    # Get chat history for the current user
    chat_history = ChatbotSession.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'chatbot/chat.html', {'chat_history': chat_history})
