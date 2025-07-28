from sklearn.cluster import KMeans
from django.contrib.auth.models import User
from users.models import UserProfile
from content.models import Lesson
from quizzes.models import UserProgress
from django.db.models import Avg, Count

def update_user_clusters():
    """
    Run K-means clustering on user learning data
    Features: lessons_completed, avg_quiz_score, subject_preference, age_group
    """
    
    # Collect user data
    users_data = []
    user_ids = []
    for user in User.objects.all():
        try:
            profile = user.userprofile
            progress = UserProgress.objects.filter(user=user)
            
            features = [
                progress.filter(completed=True).count(),  # lessons completed
                progress.aggregate(Avg('quiz_score'))['quiz_score__avg'] or 0,  # avg score
                profile.age,  # age group
                profile.preferred_subjects.count()  # subject diversity
            ]
            users_data.append(features)
            user_ids.append(user.id)
        except UserProfile.DoesNotExist:
            continue # Skip users without a profile
    
    if not users_data:
        return # No data to cluster

    # Apply K-means clustering
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(users_data)
    
    # Update user profiles with cluster assignments
    for i, user_id in enumerate(user_ids):
        profile = UserProfile.objects.get(user_id=user_id)
        profile.cluster_group = clusters[i]
        profile.save()