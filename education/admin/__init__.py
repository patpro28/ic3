from django.contrib import admin

# ModelAdmin classes
from .question import QuestionAdmin
from .category import CategoryAdmin, LevelAdmin

# Model classes
from education.models import Question, Answer, Category, Level

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Level, LevelAdmin)