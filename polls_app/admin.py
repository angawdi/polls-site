# another way to import things
# from . import models
# admin.site.register(models.Question)
# admin.site.register(models.Choice)

from django.contrib import admin
from .models import Choice, Question

# Change the header of the admin site
admin.AdminSite.site_header = 'My Awesome Polls Panel!'

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldset = [
		('Question Information', {'fields': ['question_text']}),
		('Date and Time', {'fields': ['pub_date']}), 
	]

	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
