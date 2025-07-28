# Sika.ai Product Requirements Document (PRD)

## Project Overview

**Product Name**: Sika.ai  
**Project Type**: AI-powered gamified learning web platform for children  
**Target Users**: Children aged 3-10 years in Nepal  
**Tech Stack**: Django, Python, HTML5, CSS3, Bootstrap, JavaScript, SQLite, Scikit-learn  
**Development Timeline**: Academic project (Final Year)  

## Vision Statement

Transform children's screen time into engaging, gamified educational experiences through an AI-powered learning platform that focuses on interactive learning of random topics with badges, levels, and rewards rather than rigid curriculum structure.

## Core Technical Requirements

### MVP Scope Decisions
- **Language**: English-only MVP
- **Connectivity**: Online-only (no offline functionality for MVP)
- **AI Integration**: OpenAI API for chatbot + K-means clustering for recommendations
- **Gamification**: Badge system, levels, and rewards with category-based organization
- **Learning Style**: Interactive quizzes and mini-games, minimal reading-heavy content

---

## User Stories & Acceptance Criteria

### Epic 1: User Management System

#### User Story 1.1: User Registration
**As a** child user  
**I want to** create an account with basic information  
**So that I can** access gamified learning content and track my badges  

**Acceptance Criteria:**
- User can register with: username, age, favorite topics/interests
- Age validation (3-10 years only)
- Simple, child-friendly registration form with fun visuals
- Automatic user profile creation with starter badge upon registration

#### User Story 1.2: User Authentication
**As a** registered user  
**I want to** log in securely  
**So that I can** access my learning progress, badges, and rewards  

**Acceptance Criteria:**
- Simple login with username/password
- Session management for logged-in users
- Redirect to gamified dashboard showing badges and levels after login
- Logout functionality

### Epic 2: Gamified Learning Content System

#### User Story 2.1: Category-Based Topic Exploration
**As a** child user  
**I want to** explore different topic categories  
**So that I can** discover fun, random educational content  

**Acceptance Criteria:**
- Categories include: Animals, Space, Numbers & Math, Science Fun, Geography, Inventions, Art & Colors
- Each category displays with fun icons and visual representations
- Age-appropriate content filtering (3-5, 6-8, 9-10 years)
- Optional levels within categories (if easy to implement)
- Random topic suggestions within each category

#### User Story 2.2: Interactive Quizzes
**As a** child user  
**I want to** take fun quizzes on random topics  
**So that I can** earn badges and level up while learning  

**Acceptance Criteria:**
- Multiple choice questions with visual elements (images, emojis)
- Immediate feedback with encouraging messages
- Badge rewards for quiz completion and high scores
- Quiz results contribute to user level progression
- Variety of quiz types: true/false, picture matching, simple math

#### User Story 2.3: Mini-Games
**As a** child user  
**I want to** play educational mini-games  
**So that I can** learn through interactive play and earn rewards  

**Acceptance Criteria:**
- Simple drag-and-drop games (matching animals to habitats, numbers to quantities)
- Color matching and pattern recognition games
- Simple math games (counting, basic addition/subtraction)
- Geography games (matching flags to countries, animals to continents)
- Each completed mini-game awards points toward badges

### Epic 3: Gamification System

#### User Story 3.1: Badge System
**As a** child user  
**I want to** earn badges for my achievements  
**So that I can** see my progress and feel motivated to continue learning  

**Acceptance Criteria:**
- Badge categories: Topic Explorer, Quiz Master, Mini-Game Champion, Daily Learner, Perfect Score
- Visual badge collection display on user profile
- Badge popup animations when earned
- Different badge levels (Bronze, Silver, Gold) for repeated achievements
- Special themed badges for different categories (Space Explorer, Animal Expert, Math Wizard)

#### User Story 3.2: Level System
**As a** child user  
**I want to** level up as I complete activities  
**So that I can** unlock new content and feel progression  

**Acceptance Criteria:**
- User level increases based on points from completed activities
- Level progression bar visible on dashboard
- New categories or content unlocked at certain levels (if easy to implement)
- Level-up animations and celebrations
- Each level requires progressively more points

#### User Story 3.3: Rewards and Progress Tracking
**As a** child user  
**I want to** see my achievements and rewards  
**So that I can** track my learning journey and stay motivated  

**Acceptance Criteria:**
- Dashboard showing total badges, current level, and recent achievements
- Daily streak counter for consecutive days of learning
- Simple statistics: topics explored, quizzes completed, games played
- Virtual trophy case displaying all earned badges
- Progress celebration animations

### Epic 4: AI-Powered Features

#### User Story 4.1: AI Learning Buddy
**As a** child user  
**I want to** ask questions to a friendly AI companion  
**So that I can** get help and learn about topics that interest me  

**Acceptance Criteria:**
- Simple chat interface with large, child-friendly buttons
- AI responses are encouraging and educational
- AI can suggest new topics based on user interests
- Chat interactions contribute to "Curious Explorer" badges
- Error handling with friendly fallback messages

#### User Story 4.2: Smart Topic Recommendations
**As a** child user  
**I want to** get personalized topic suggestions  
**So that I can** discover new interesting things to learn  

**Acceptance Criteria:**
- Recommendations based on completed categories and quiz performance
- Mix of similar topics and new discoveries
- "Surprise Me!" button for completely random topic selection
- Recommendations update based on user engagement patterns
- Visual recommendation cards with topic previews

### Epic 5: Admin Content Management

#### User Story 5.1: Gamified Content Administration
**As an** admin  
**I want to** manage educational content and gamification elements  
**So that I can** create engaging learning experiences  

**Acceptance Criteria:**
- Django admin interface for managing topics, quizzes, and mini-games
- Ability to create badge criteria and rewards
- Upload images and visual content for topics
- Set difficulty levels and age appropriateness
- Manage point values and level thresholds

#### User Story 5.2: Gamification Analytics
**As an** admin  
**I want to** view user engagement and gamification metrics  
**So that I can** understand what motivates learning  

**Acceptance Criteria:**
- Dashboard showing badge distribution and user levels
- Most popular categories and topics
- User engagement patterns and session lengths
- Badge earning rates and progression analytics

---

## Technical Specifications

### Database Models

#### User Profile Model (Extended)
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(10)])
    favorite_topics = models.ManyToManyField('TopicCategory', blank=True)
    current_level = models.IntegerField(default=1)
    total_points = models.IntegerField(default=0)
    daily_streak = models.IntegerField(default=0)
    last_activity_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cluster_group = models.IntegerField(null=True, blank=True)
```

#### Topic Category Model
```python
class TopicCategory(models.Model):
    name = models.CharField(max_length=50)  # Animals, Space, Numbers, etc.
    description = models.TextField()
    icon = models.CharField(max_length=50)  # Font Awesome icon class
    color_theme = models.CharField(max_length=7)  # Hex color code
    age_groups = models.CharField(max_length=20)
    unlock_level = models.IntegerField(default=1)  # Level required to unlock
```

#### Random Topic Model
```python
class RandomTopic(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(TopicCategory, on_delete=models.CASCADE)
    content = models.TextField()  # Brief, engaging content
    fun_fact = models.TextField()  # Interesting fact about the topic
    age_group = models.CharField(max_length=10)
    image = models.ImageField(upload_to='topics/', blank=True)
    difficulty_level = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')])
    created_at = models.DateTimeField(auto_now_add=True)
```

#### Quiz Model (Enhanced)
```python
class Quiz(models.Model):
    topic = models.ForeignKey(RandomTopic, on_delete=models.CASCADE)
    question = models.TextField()
    question_image = models.ImageField(upload_to='quiz_images/', blank=True)
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200, blank=True)  # Optional 4th option
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    points_value = models.IntegerField(default=10)
    explanation = models.TextField(blank=True)  # Brief explanation of correct answer
```

#### Mini Game Model
```python
class MiniGame(models.Model):
    GAME_TYPES = [
        ('drag_drop', 'Drag and Drop'),
        ('matching', 'Matching Game'),
        ('sorting', 'Sorting Game'),
        ('counting', 'Counting Game'),
    ]
    
    name = models.CharField(max_length=100)
    game_type = models.CharField(max_length=20, choices=GAME_TYPES)
    category = models.ForeignKey(TopicCategory, on_delete=models.CASCADE)
    instructions = models.TextField()
    game_data = models.JSONField()  # Store game-specific data
    points_value = models.IntegerField(default=15)
    age_group = models.CharField(max_length=10)
```

#### Badge Model
```python
class Badge(models.Model):
    BADGE_TYPES = [
        ('topic_explorer', 'Topic Explorer'),
        ('quiz_master', 'Quiz Master'),
        ('game_champion', 'Game Champion'),
        ('daily_learner', 'Daily Learner'),
        ('perfect_score', 'Perfect Score'),
        ('category_expert', 'Category Expert'),
    ]
    
    BADGE_LEVELS = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES)
    badge_level = models.CharField(max_length=10, choices=BADGE_LEVELS)
    icon = models.CharField(max_length=50)  # Font Awesome icon
    criteria = models.JSONField()  # Criteria for earning the badge
    points_required = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
```

#### User Badge Model
```python
class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    progress_data = models.JSONField(blank=True, null=True)  # Progress toward next level
    
    class Meta:
        unique_together = ['user', 'badge']
```

#### Activity Log Model
```python
class ActivityLog(models.Model):
    ACTIVITY_TYPES = [
        ('quiz_completed', 'Quiz Completed'),
        ('game_played', 'Mini Game Played'),
        ('topic_explored', 'Topic Explored'),
        ('badge_earned', 'Badge Earned'),
        ('level_up', 'Level Up'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    points_earned = models.IntegerField(default=0)
    details = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Django Apps Structure

#### apps/users/
- User registration, authentication, profiles
- UserProfile model with gamification data
- Badge collection and level management

#### apps/topics/
- RandomTopic and TopicCategory models
- Category browsing and topic exploration
- Random topic generation

#### apps/quizzes/
- Enhanced Quiz model with gamification
- Quiz-taking with point rewards
- Progress tracking and badge triggers

#### apps/games/
- MiniGame model and game engine
- Interactive game implementations
- Game completion tracking

#### apps/gamification/
- Badge system implementation
- Level progression logic
- Point calculation and rewards

#### apps/chatbot/
- AI learning buddy integration
- Topic suggestion through AI
- Educational chat responses

#### apps/analytics/
- User engagement tracking
- Gamification metrics
- Recommendation engine with clustering

### Key Gamification Features Implementation

#### Badge System
```python
# Location: apps/gamification/badge_manager.py
class BadgeManager:
    @staticmethod
    def check_and_award_badges(user, activity_type, activity_data):
        """
        Check if user qualifies for any badges based on recent activity
        """
        available_badges = Badge.objects.filter(is_active=True)
        newly_earned = []
        
        for badge in available_badges:
            if BadgeManager.meets_criteria(user, badge, activity_type, activity_data):
                user_badge, created = UserBadge.objects.get_or_create(
                    user=user, 
                    badge=badge
                )
                if created:
                    newly_earned.append(badge)
                    # Award points for earning badge
                    user.userprofile.total_points += badge.points_required
                    user.userprofile.save()
        
        return newly_earned
    
    @staticmethod
    def meets_criteria(user, badge, activity_type, activity_data):
        """
        Check if user meets specific badge criteria
        """
        criteria = badge.criteria
        
        if badge.badge_type == 'quiz_master':
            completed_quizzes = ActivityLog.objects.filter(
                user=user, 
                activity_type='quiz_completed'
            ).count()
            return completed_quizzes >= criteria.get('quizzes_required', 10)
        
        elif badge.badge_type == 'perfect_score':
            return (activity_type == 'quiz_completed' and 
                    activity_data.get('score', 0) == 100)
        
        # Add more badge criteria logic here
        return False
```

#### Level Progression System
```python
# Location: apps/gamification/level_manager.py
class LevelManager:
    LEVEL_THRESHOLDS = [0, 100, 250, 500, 800, 1200, 1700, 2300, 3000, 4000, 5000]
    
    @staticmethod
    def calculate_level(total_points):
        """
        Calculate user level based on total points
        """
        for level, threshold in enumerate(LevelManager.LEVEL_THRESHOLDS):
            if total_points < threshold:
                return level
        return len(LevelManager.LEVEL_THRESHOLDS)
    
    @staticmethod
    def check_level_up(user, points_earned):
        """
        Check if user leveled up and trigger celebrations
        """
        profile = user.userprofile
        old_level = profile.current_level
        new_level = LevelManager.calculate_level(profile.total_points)
        
        if new_level > old_level:
            profile.current_level = new_level
            profile.save()
            
            # Log level up activity
            ActivityLog.objects.create(
                user=user,
                activity_type='level_up',
                points_earned=0,
                details={'old_level': old_level, 'new_level': new_level}
            )
            
            return True
        return False
```

#### Random Topic Recommendation
```python
# Location: apps/topics/recommendation_engine.py
def get_topic_recommendations(user, category=None, count=5):
    """
    Get personalized topic recommendations with gamification elements
    """
    profile = user.userprofile
    
    # Get user's activity history
    completed_topics = ActivityLog.objects.filter(
        user=user,
        activity_type='topic_explored'
    ).values_list('details__topic_id', flat=True)
    
    # Base query excluding completed topics
    topics_query = RandomTopic.objects.exclude(
        id__in=completed_topics
    ).filter(
        age_group__contains=str(profile.age)[:1]  # Match age group
    )
    
    if category:
        topics_query = topics_query.filter(category=category)
    
    # Prioritize topics that match user's favorite categories
    favorite_topics = topics_query.filter(
        category__in=profile.favorite_topics.all()
    )[:count//2]
    
    # Add some random topics for variety
    random_topics = topics_query.exclude(
        category__in=profile.favorite_topics.all()
    ).order_by('?')[:count - len(favorite_topics)]
    
    return list(favorite_topics) + list(random_topics)
```

### Frontend Gamification Elements

#### Dashboard Template Structure
```html
<!-- templates/users/dashboard.html -->
<div class="gamified-dashboard">
    <!-- Level Progress Bar -->
    <div class="level-section">
        <h3>Level {{ user.userprofile.current_level }}</h3>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {{ level_progress }}%"></div>
        </div>
        <p>{{ points_to_next_level }} points to next level!</p>
    </div>
    
    <!-- Badge Collection -->
    <div class="badge-collection">
        <h4>My Badges ({{ user_badges.count }})</h4>
        <div class="badge-grid">
            {% for user_badge in user_badges %}
            <div class="badge-item {{ user_badge.badge.badge_level }}">
                <i class="{{ user_badge.badge.icon }}"></i>
                <span>{{ user_badge.badge.name }}</span>
            </div>
            {% endfor %}
        </div>
    </div>
    
    <!-- Topic Categories -->
    <div class="category-grid">
        {% for category in topic_categories %}
        <div class="category-card" style="border-color: {{ category.color_theme }}">
            <i class="{{ category.icon }}"></i>
            <h5>{{ category.name }}</h5>
            <a href="{% url 'explore_category' category.id %}" class="btn btn-primary">
                Explore!
            </a>
        </div>
        {% endfor %}
    </div>
</div>
```

### URL Structure

```python
# Main urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('topics.urls')),              # Homepage, topic exploration
    path('users/', include('users.urls')),         # Login, register, profile, badges
    path('quiz/', include('quizzes.urls')),        # Quiz taking with gamification
    path('games/', include('games.urls')),         # Mini-games interface
    path('chat/', include('chatbot.urls')),        # AI learning buddy
    path('gamification/', include('gamification.urls')), # Badge/level management
    path('analytics/', include('analytics.urls')), # Admin dashboard
]

# apps/topics/urls.py
urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('category/<int:category_id>/', views.CategoryView.as_view(), name='explore_category'),
    path('topic/<int:topic_id>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('random-topic/', views.RandomTopicView.as_view(), name='random_topic'),
]

# apps/quizzes/urls.py
urlpatterns = [
    path('topic/<int:topic_id>/', views.QuizView.as_view(), name='take_quiz'),
    path('results/<int:quiz_session_id>/', views.QuizResultsView.as_view(), name='quiz_results'),
]

# apps/games/urls.py
urlpatterns = [
    path('', views.GameListView.as_view(), name='game_list'),
    path('<int:game_id>/', views.GamePlayView.as_view(), name='play_game'),
    path('complete/<int:game_id>/', views.GameCompleteView.as_view(), name='game_complete'),
]
```

### Frontend Requirements

#### Templates Structure
```
templates/
├── base.html                    # Bootstrap base template with gamification elements
├── topics/
│   ├── dashboard.html          # Gamified dashboard with badges/levels
│   ├── category_list.html      # Category exploration page
│   ├── topic_detail.html       # Individual topic with fun facts
│   ├── random_topic.html       # Surprise topic discovery
├── users/
│   ├── register.html           # Child-friendly registration
│   ├── login.html              # Simple login form
│   ├── profile.html            # Badge collection and progress
│   ├── badge_detail.html       # Individual badge information
├── quizzes/
│   ├── quiz.html               # Gamified quiz interface
│   ├── results.html            # Results with badge rewards
├── games/
│   ├── game_list.html          # Available mini-games
│   ├── drag_drop_game.html     # Drag and drop game template
│   ├── matching_game.html      # Matching game template
│   ├── game_complete.html      # Game completion with rewards
├── chatbot/
│   └── chat.html               # AI learning buddy interface
└── analytics/
    └── dashboard.html          # Admin analytics dashboard
```

#### Key UI Components
- **Gamified Dashboard**: Level progress bars, badge displays, category cards
- **Child-friendly design**: Large buttons, bright colors, animated feedback
- **Bootstrap responsive layout**: Tablet and smartphone optimized
- **Progress indicators**: Visual feedback on achievements and progression
- **Interactive elements**: Hover effects, click animations, reward celebrations
- **Simple navigation**: Clear icons and minimal text for young users

### Development Priorities

#### Phase 1: Core Platform Foundation (Week 1-2)
1. **Django Setup & Models**
   - Create all Django apps with proper structure
   - Implement core models: UserProfile, TopicCategory, RandomTopic, Badge
   - Set up Django admin interface for content management
   - Configure database migrations and initial data

2. **Basic User System**
   - User registration with gamification setup (starter badge)
   - Authentication system with child-friendly interface
   - Basic profile management with badge display

3. **Content Foundation**
   - Topic category browsing system
   - Random topic display with basic content
   - Simple quiz functionality without advanced gamification

#### Phase 2: Gamification & Interactivity (Week 3-4)
1. **Gamification Engine**
   - Implement badge system with criteria checking
   - Build level progression logic with point calculation
   - Create activity logging system
   - Add reward feedback system (popups, animations)

2. **Interactive Learning**
   - Build quiz system with point rewards and badge triggers
   - Implement basic mini-games (drag-drop, matching)
   - Add immediate feedback and celebration animations
   - Create progress tracking across all activities

3. **AI Integration**
   - Integrate OpenAI chatbot as learning buddy
   - Implement topic recommendations based on user behavior
   - Add K-means clustering for user grouping

#### Phase 3: Advanced Features & Polish (Week 5-6)
1. **Advanced Gamification**
   - Implement daily streaks and bonus rewards
   - Add more complex badge criteria and progression
   - Create leaderboards or social elements (if desired)
   - Fine-tune point balancing and level thresholds

2. **Content & Analytics**
   - Expand mini-game variety
   - Build admin analytics dashboard
   - Implement recommendation refinements
   - Add content management tools for admins

3. **Testing & Optimization**
   - Comprehensive testing of all gamification elements
   - UI/UX improvements based on testing
   - Performance optimization
   - Bug fixes and edge case handling

### Environment Variables

```bash
# .env file
SECRET_KEY=your-django-secret-key
DEBUG=True
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=sqlite:///db.sqlite3  # For development
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Success Metrics

#### Technical Metrics
- All user stories implemented and tested
- Badge system correctly awards based on user activities
- Level progression works smoothly with point accumulation
- K-means clustering successfully groups users for recommendations
- OpenAI chatbot responds to 95%+ of queries with child-appropriate content
- Mini-games function without bugs across different devices

#### Gamification Metrics
- User engagement: average session time > 15 minutes
- Badge earning rate: users earn at least 1 badge per week
- Level progression: 70% of users reach level 3 within first month
- Category exploration: users explore at least 3 different categories
- Daily streak maintenance > 3 days average

#### Learning Metrics
- Topic completion rate > 60%
- Quiz performance improvement over time
- Positive AI chatbot interaction experience
- Accurate recommendations lead to topic exploration

---

## Development Guidelines for Roo AI

### When Building Features:
1. **Start with models** - Define database structure first, focusing on gamification relationships
2. **Create simple views** - Build functionality incrementally, test each component
3. **Use Django admin** - Leverage built-in admin for content and badge management
4. **Test gamification logic** - Verify badge awards, point calculations, and level progression
5. **Keep it simple initially** - Get basic gamification working before adding complexity
6. **Focus on user feedback** - Ensure users always see immediate results from their actions

### Code Standards:
- **Follow Django best practices** and conventions
- **Use class-based views** where appropriate, especially for gamified interactions
- **Implement proper error handling** for AI API calls and gamification edge cases
- **Add docstrings** to complex functions, especially gamification algorithms and ML code
- **Use Django's built-in authentication** system with custom UserProfile extension
- **Maintain consistent naming** conventions across gamification elements

### Specific Coding Guidelines:

#### Model Design:
```python
# Good: Clear relationships and validation
class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'badge']  # Prevent duplicate badges
        
    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"
```

#### View Structure:
```python
# Use mixins for common gamification functionality
class GamificationMixin:
    def award_points_and_check_badges(self, user, points, activity_type, activity_data):
        """Common method to handle point awards and badge checking"""
        profile = user.userprofile
        profile.total_points += points
        profile.save()
        
        # Check for new badges
        new_badges = BadgeManager.check_and_award_badges(user, activity_type, activity_data)
        
        # Check for level up
        level_up = LevelManager.check_level_up(user, points)
        
        return {'new_badges': new_badges, 'level_up': level_up, 'points_earned': points}
```

#### Template Organization:
```html
<!-- Use consistent structure for gamification elements -->
{% load gamification_tags %}  <!-- Custom template tags for badges/levels -->

<div class="gamification-panel">
    {% user_level user %}
    {% user_badges user %}
    {% recent_achievements user %}
</div>
```

### Testing Strategy:

#### Unit Tests:
```python
# Test gamification logic thoroughly
class BadgeSystemTest(TestCase):
    def test_quiz_master_badge_awarded(self):
        """Test that Quiz Master badge is awarded after completing required quizzes"""
        user = User.objects.create_user('testuser', 'test@test.com', 'password')
        
        # Complete required number of quizzes
        for i in range(10):
            ActivityLog.objects.create(
                user=user,
                activity_type='quiz_completed',
                points_earned=10
            )
        
        # Check badge is awarded
        badges = BadgeManager.check_and_award_badges(user, 'quiz_completed', {})
        self.assertTrue(any(b.badge_type == 'quiz_master' for b in badges))
    
    def test_level_progression(self):
        """Test that user levels up correctly based on points"""
        user = User.objects.create_user('testuser', 'test@test.com', 'password')
        profile = user.userprofile
        profile.total_points = 250  # Should be level 3
        profile.save()
        
        level = LevelManager.calculate_level(250)
        self.assertEqual(level, 3)
```

#### Integration Tests:
- Test complete user flows: registration → quiz taking → badge earning → level up
- Verify AI chatbot integration works with fallback handling
- Test recommendation system with sample user data
- Ensure gamification elements display correctly in templates

#### Manual Testing Checklist:
- [ ] User can register and receive starter badge
- [ ] Quizzes award correct points and trigger appropriate badges
- [ ] Level progression displays correctly with animations
- [ ] Mini-games function properly and award rewards
- [ ] AI chatbot provides appropriate responses for children
- [ ] Admin can manage content through Django admin
- [ ] Responsive design works on tablets and phones
- [ ] All gamification animations and feedback work smoothly

### Performance Considerations:
- **Optimize badge checking** - Don't check all badges on every activity
- **Cache user statistics** - Store computed values like total badges, current level
- **Efficient queries** - Use select_related and prefetch_related for gamification data
- **API rate limiting** - Handle OpenAI API limits gracefully
- **Image optimization** - Compress topic and badge images for faster loading

### Error Handling:
```python
# Always handle AI API failures gracefully
def get_ai_response(question):
    try:
        response = openai_client.chat.completions.create(...)
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return "I'm having trouble thinking right now! Try asking me something else!"
    except Exception as e:
        logger.error(f"Unexpected error in AI response: {e}")
        return "Oops! Something went wrong. Let's try again!"
```

### Deployment Checklist:
- [ ] All environment variables configured
- [ ] Database migrations applied
- [ ] Static files collected and served properly
- [ ] OpenAI API key working and rate limits understood
- [ ] Admin superuser created for content management
- [ ] Sample content loaded (topics, categories, badges)
- [ ] Error logging configured
- [ ] Backup strategy in place for user progress and badges

This PRD provides a complete roadmap for building your gamified Sika.ai platform with clear technical guidance, testing strategies, and development best practices specifically tailored for working with Roo AI. Focus on implementing features in the priority order listed, always testing gamification elements thoroughly as they're core to user engagement.