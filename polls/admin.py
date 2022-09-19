from django.contrib import admin
from . models import Question, Answer, Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('question_text', 'pub_date', 'type')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_answer', 'question')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question','votes')

# Register your models here.
