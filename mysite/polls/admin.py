from django.contrib import admin

from .models import Question
from .models import Choice #added by Mahmoud to test chocie

admin.site.register(Question)
admin.site.register(Choice) #added by Mahmoud to test chocie
