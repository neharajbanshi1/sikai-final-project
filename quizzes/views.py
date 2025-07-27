from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from content.models import Lesson
from .models import Quiz, UserProgress

@login_required
def quiz_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    quizzes = Quiz.objects.filter(lesson=lesson)
    
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
        
        # Save user progress
        UserProgress.objects.update_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'completed': True, 'quiz_score': percentage_score}
        )
        
        # Store answers in session to show on results page
        request.session['quiz_answers'] = user_answers
        
        return redirect('quiz_results', lesson_id=lesson.id)
        
    return render(request, 'quizzes/quiz.html', {'lesson': lesson, 'quizzes': quizzes})

@login_required
def quiz_results(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    progress = get_object_or_404(UserProgress, user=request.user, lesson=lesson)
    quizzes = Quiz.objects.filter(lesson=lesson)
    
    # Get answers from session
    user_answers = request.session.get('quiz_answers', {})
    
    # Convert keys to integers for template comparison
    user_answers = {int(k): v for k, v in user_answers.items()}

    context = {
        'lesson': lesson,
        'progress': progress,
        'quizzes': quizzes,
        'user_answers': user_answers,
    }
    
    return render(request, 'quizzes/results.html', context)