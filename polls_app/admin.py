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
		('Date and Time', {'fields': ['pub_data']}), 
	]

	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_data', 'was_published_recently')
	list_filter = ['pub_data']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
