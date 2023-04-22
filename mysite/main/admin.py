from django.contrib import admin
from .models import MyUser
# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name']
    list_display_links = ['id', 'user_name']
    search_fields = ['user_name']