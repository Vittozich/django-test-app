from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.site_header = "Панель администратора"
admin.site.site_title = "Админка"
admin.site.index_title = "Добро пожаловать в панель администратора"

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields':['question_text']}),
              ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
              ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


# admin.site.register(Question)
# admin.site.register(Choice)