from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """
    The first element of each tuple in fieldsets is the title of the fieldset. Here’s what our form looks like now:
    """
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {'fields': ['pub_date']}), ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_per_page = 10
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
