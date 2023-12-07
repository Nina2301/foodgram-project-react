from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'get_recipe_count',
        'get_subscriber_count',
    )
    list_filter = ('email', 'first_name')
    empty_value_display = '-пусто-'

    @admin.display(description='Количество рецептов')
    def get_recipe_count(self, obj):
        return obj.recipes.count()

    @admin.display(description='Количество подписчиков')
    def get_subscriber_count(self, obj):
        return obj.subscriber.count()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.unregister(TokenProxy)
