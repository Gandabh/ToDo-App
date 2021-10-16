from django.contrib import admin
from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','complete','created_at')  
    list_filter = ('title','complete','created_at')  
    search_fields = ('title','complete','created_at')  

