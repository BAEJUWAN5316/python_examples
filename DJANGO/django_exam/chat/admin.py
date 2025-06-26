from django.contrib import admin
from .models import PuzzleRoom

# Register your models here.

@admin.register(PuzzleRoom)
class PuzzleRoomAdmin(admin.ModelAdmin):
    pass