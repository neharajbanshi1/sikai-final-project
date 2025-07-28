from django.contrib.auth.models import User
from content.models import Lesson
from django.db.models import Count

def get_recommendations(user, limit=5):
    """
    Get lesson recommendations based on user's cluster group
    """
    try:
        user_cluster = user.userprofile.cluster_group
        if user_cluster is None:
            return Lesson.objects.none() # No cluster assigned
    except User.userprofile.RelatedObjectDoesNotExist:
        return Lesson.objects.none() # No profile for user

    # Find users in the same cluster
    similar_users = User.objects.filter(userprofile__cluster_group=user_cluster).exclude(id=user.id)
    
    if not similar_users.exists():
        return Lesson.objects.order_by('?')[:limit] # Return random lessons if no similar users

    # Find lessons popular among similar users that the current user has not completed
    completed_lessons = user.userprogress_set.filter(completed=True).values_list('lesson_id', flat=True)
    
    popular_lessons = Lesson.objects.filter(
        userprogress__user__in=similar_users,
        userprogress__completed=True
    ).exclude(
        id__in=completed_lessons
    ).annotate(
        popularity=Count('userprogress')
    ).order_by('-popularity')[:limit]
    
    return popular_lessons