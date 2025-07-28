from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from content.models import RandomTopic
from .models import Quiz

@login_required
def quiz_view(request, topic_id):
    topic = get_object_or_404(RandomTopic, id=topic_id)
    quizzes = Quiz.objects.filter(topic=topic)
    
    if request.method == 'POST':
        score = 0
        total_questions = quizzes.count()
        user_answers = {}

        for quiz in quizzes:
            selected_option = request.POST.get(f'question_{quiz.id}')
            user_answers[quiz.id] = selected_option
            if selected_option == quiz.correct_answer:
                score += 1
        
        percentage_score = (score / total_questions) * 100 if total_questions > 0 else 0
        
        # Store answers in session to show on results page
        request.session['quiz_answers'] = user_answers
        request.session['quiz_score'] = percentage_score
        
        return redirect('quiz_results', topic_id=topic.id)
        
    return render(request, 'quizzes/quiz.html', {'topic': topic, 'quizzes': quizzes})

@login_required
def quiz_results(request, topic_id):
    topic = get_object_or_404(RandomTopic, id=topic_id)
    quizzes = Quiz.objects.filter(topic=topic)
    
    # Get answers from session
    user_answers = request.session.get('quiz_answers', {})
    score = request.session.get('quiz_score', 0)
    
    # Convert keys to integers for template comparison
    user_answers = {int(k): v for k, v in user_answers.items()}

    context = {
        'topic': topic,
        'score': score,
        'quizzes': quizzes,
        'user_answers': user_answers,
    }
    
    return render(request, 'quizzes/results.html', context)