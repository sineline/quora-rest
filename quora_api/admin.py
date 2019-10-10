from django.contrib import admin
from quora_api.models import (
    Question,
    Answer,
    Like
)

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)