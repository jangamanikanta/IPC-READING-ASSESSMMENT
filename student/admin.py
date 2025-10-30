from django.contrib import admin
from .models import PassageModel

# Register your models here.
class PassageAdmin(admin.ModelAdmin):
    list_display = ['id','passage']


admin.site.register(PassageModel,PassageAdmin)