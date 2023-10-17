from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    list_filter = ('email', 'first_name')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
