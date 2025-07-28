from django.contrib import admin
from .models import Badge, UserBadge, ActivityLog

# Register your models here.
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(ActivityLog)
