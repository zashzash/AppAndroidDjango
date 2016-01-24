from django.contrib import admin

# Register your models here.
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)
    
admin.site.register(Question,QuestionAdmin)
