# Sika.ai Product Requirements Document (PRD)

## Project Overview

**Product Name**: Sika.ai  
**Project Type**: AI-powered educational web platform for children  
**Target Users**: Children aged 3-10 years in Nepal  
**Tech Stack**: Django, Python, HTML5, CSS3, Bootstrap, JavaScript, SQLite, Scikit-learn  
**Development Timeline**: Academic project (Final Year)  

## Vision Statement

Transform children's screen time into meaningful educational experiences through an AI-powered learning platform that provides personalized content recommendations and interactive chatbot assistance.

## Core Technical Requirements

### MVP Scope Decisions
- **Language**: English-only MVP
- **Connectivity**: Online-only (no offline functionality for MVP)
- **AI Integration**: OpenAI API for chatbot + K-means clustering for recommendations
- **Analytics**: Minimal tracking with basic admin dashboard

---

## User Stories & Acceptance Criteria

### Epic 1: User Management System

#### User Story 1.1: User Registration
**As a** child user  
**I want to** create an account with basic information  
**So that I can** access personalized learning content  

**Acceptance Criteria:**
- User can register with: username, age, preferred subjects
- Age validation (3-14 years only)
- Simple, child-friendly registration form
- Automatic user profile creation upon registration

#### User Story 1.2: User Authentication
**As a** registered user  
**I want to** log in securely  
**So that I can** access my learning progress and recommendations  

**Acceptance Criteria:**
- Simple login with username/password
- Session management for logged-in users
- Redirect to age-appropriate dashboard after login
- Logout functionality

### Epic 2: Educational Content Management

#### User Story 2.1: Lesson Access
**As a** child user  
**I want to** browse and access educational lessons  
**So that I can** learn different subjects  

**Acceptance Criteria:**
- Lessons organized by subjects (Math, Science, Language, Art)
- Age-appropriate content filtering (3-5, 6-8, 9-10 years)
- Lesson content includes text, images, and simple explanations
- Progress tracking when lesson is completed

#### User Story 2.2: Interactive Quizzes
**As a** child user  
**I want to** take quizzes after lessons  
**So that I can** test my understanding and see my progress  

**Acceptance Criteria:**
- Multiple choice questions related to lesson content
- Immediate feedback on answers (correct/incorrect)
- Quiz results saved to user profile
- Simple scoring system (percentage correct)

### Epic 3: AI-Powered Features

#### User Story 3.1: AI Chatbot Assistant
**As a** child user  
**I want to** ask questions to an AI tutor  
**So that I can** get help with learning topics  

**Acceptance Criteria:**
- Simple chat interface with text input
- Integration with OpenAI API for responses
- Child-friendly, educational responses only
- Chat history saved during session
- Error handling for API failures

#### User Story 3.2: Personalized Recommendations
**As a** child user  
**I want to** receive lesson recommendations based on my learning patterns  
**So that I can** discover content that matches my interests and abilities  

**Acceptance Criteria:**
- K-means clustering algorithm groups users by learning behavior
- Recommendations shown on user dashboard
- Based on: completed lessons, quiz scores, subject preferences, age group
- Minimum 3-5 lesson recommendations per user
- Recommendations update weekly

### Epic 4: Admin Content Management

#### User Story 4.1: Content Administration
**As an** admin  
**I want to** manage educational content through Django admin  
**So that I can** add, edit, and organize lessons and quizzes  

**Acceptance Criteria:**
- Django admin interface for content management
- Ability to create/edit lessons with rich text
- Upload images for lesson content
- Create and manage quiz questions
- Categorize content by subject and age group

#### User Story 4.2: User Analytics Dashboard
**As an** admin  
**I want to** view basic user analytics  
**So that I can** understand platform usage and learning patterns  

**Acceptance Criteria:**
- Simple dashboard showing: total users, lessons completed, quiz performance
- Basic charts showing subject popularity
- User progress overview
- K-means clustering results visualization

---

## Technical Specifications

### Database Models

#### User Model (Extends Django User)
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(10)])
    preferred_subjects = models.ManyToManyField('Subject', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cluster_group = models.IntegerField(null=True, blank=True)  # For K-means
```

#### Subject Model
```python
class Subject(models.Model):
    name = models.CharField(max_length=50)  # Math, Science, Language, Art
    description = models.TextField()
    age_groups = models.CharField(max_length=20)  # "3-5", "6-8", "9-10"
```

#### Lesson Model
```python
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    age_group = models.CharField(max_length=10)
    difficulty_level = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    image = models.ImageField(upload_to='lessons/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Quiz Model
```python
class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
```

#### User Progress Model
```python
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    quiz_score = models.FloatField(null=True, blank=True)  # Percentage score
    time_spent = models.DurationField(null=True, blank=True)
    completed_at = models.DateTimeField(auto_now_add=True)
```

#### Chatbot Session Model
```python
class ChatbotSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

### Django Apps Structure

#### apps/users/
- User registration, authentication, profiles
- UserProfile model and forms
- Login/logout views

#### apps/content/
- Lesson and Subject models
- Content browsing and display views
- Homepage and navigation

#### apps/quizzes/
- Quiz model and quiz-taking functionality
- Score calculation and storage
- Progress tracking

#### apps/chatbot/
- OpenAI API integration
- Chat interface and message handling
- Session management

#### apps/analytics/
- K-means clustering implementation
- Recommendation engine
- Admin dashboard views
- User behavior tracking

### Key Features Implementation

#### K-Means Clustering Algorithm
```python
# Location: apps/analytics/ml_engine.py
def update_user_clusters():
    """
    Run K-means clustering on user learning data
    Features: lessons_completed, avg_quiz_score, subject_preference, age_group
    """
    from sklearn.cluster import KMeans
    
    # Collect user data
    users_data = []
    for user in User.objects.all():
        profile = user.userprofile
        progress = UserProgress.objects.filter(user=user)
        
        features = [
            progress.filter(completed=True).count(),  # lessons completed
            progress.aggregate(Avg('quiz_score'))['quiz_score__avg'] or 0,  # avg score
            profile.age,  # age group
            profile.preferred_subjects.count()  # subject diversity
        ]
        users_data.append(features)
    
    # Apply K-means clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    clusters = kmeans.fit_predict(users_data)
    
    # Update user profiles with cluster assignments
    for i, user in enumerate(User.objects.all()):
        user.userprofile.cluster_group = clusters[i]
        user.userprofile.save()
```

#### Recommendation System
```python
# Location: apps/analytics/recommendations.py
def get_recommendations(user, limit=5):
    """
    Get lesson recommendations based on user's cluster group
    """
    user_cluster = user.userprofile.cluster_group
    
    # Find users in same cluster
    similar_users = User.objects.filter(userprofile__cluster_group=user_cluster)
    
    # Find lessons popular among similar users
    popular_lessons = Lesson.objects.filter(
        userprogress__user__in=similar_users,
        userprogress__completed=True
    ).annotate(
        popularity=Count('userprogress')
    ).exclude(
        userprogress__user=user  # Exclude already completed
    ).order_by('-popularity')[:limit]
    
    return popular_lessons
```

#### OpenAI Chatbot Integration
```python
# Location: apps/chatbot/ai_service.py
import openai
from django.conf import settings

def get_chatbot_response(user_question):
    """
    Get educational response from OpenAI API
    """
    try:
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful educational tutor for children aged 3-10. Provide simple, encouraging, and educational responses."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return "I'm sorry, I'm having trouble right now. Please try asking your question again later!"
```

### URL Structure

```python
# Main urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('content.urls')),           # Homepage, lessons
    path('users/', include('users.urls')),       # Login, register, profile
    path('quiz/', include('quizzes.urls')),      # Quiz taking
    path('chat/', include('chatbot.urls')),      # Chatbot interface
    path('analytics/', include('analytics.urls')), # Admin dashboard
]
```

### Frontend Requirements

#### Templates Structure
```
templates/
├── base.html                    # Bootstrap base template
├── content/
│   ├── home.html               # Dashboard with recommendations
│   ├── lesson_list.html        # Browse lessons by subject
│   ├── lesson_detail.html      # Individual lesson content
├── users/
│   ├── register.html           # Child-friendly registration
│   ├── login.html              # Simple login form
│   ├── profile.html            # User progress overview
├── quizzes/
│   ├── quiz.html               # Quiz taking interface
│   ├── results.html            # Quiz results and feedback
├── chatbot/
│   └── chat.html               # Simple chat interface
└── analytics/
    └── dashboard.html          # Admin analytics dashboard
```

#### Key UI Components
- **Child-friendly design**: Large buttons, bright colors, simple navigation
- **Bootstrap responsive layout**: Works on tablets and basic smartphones
- **Progress indicators**: Visual feedback on lesson completion
- **Simple chat interface**: Text input with send button for chatbot
- **Recommendation cards**: Visual lesson suggestions on homepage

### Development Priorities

#### Phase 1: Core Platform (Week 1-2)
1. Set up Django apps and basic models
2. User registration and authentication
3. Basic lesson browsing and content display
4. Simple quiz functionality

#### Phase 2: AI Integration (Week 3-4)
1. Implement OpenAI chatbot integration
2. Build K-means clustering algorithm
3. Create recommendation system
4. User progress tracking

#### Phase 3: Polish & Analytics (Week 5-6)
1. Admin dashboard with basic analytics
2. UI improvements and child-friendly design
3. Error handling and edge cases
4. Testing and bug fixes

### Environment Variables

```bash
# .env file
SECRET_KEY=your-django-secret-key
DEBUG=True
OPENAI_API_KEY=your-openai-api-key
```

### Success Metrics

#### Technical Metrics
- All user stories implemented and tested
- K-means clustering successfully groups users
- OpenAI chatbot responds to 95%+ of queries
- Recommendation system suggests relevant content

#### User Experience Metrics
- Simple registration process (< 2 minutes)
- Lesson completion rate > 60%
- Positive chatbot interaction experience
- Accurate recommendations based on user behavior

---

## Development Guidelines for Roo AI

### When Building Features:
1. **Start with models** - Define database structure first
2. **Create simple views** - Focus on functionality over aesthetics initially
3. **Use Django admin** - Leverage built-in admin for content management
4. **Test incrementally** - Verify each feature works before moving to next
5. **Keep it simple** - Prioritize working features over complex implementations

### Code Standards:
- Follow Django best practices and conventions
- Use class-based views where appropriate
- Implement proper error handling
- Add docstrings to complex functions (especially ML algorithms)
- Use Django's built-in authentication system

### Testing Strategy:
- Test user registration and login flows
- Verify K-means clustering with sample data
- Test OpenAI API integration with fallback responses
- Ensure recommendations update correctly

This PRD provides a complete roadmap for building your Sika.ai educational platform. Focus on implementing features in the priority order listed, and remember that a working simple version is better than a complex broken one.