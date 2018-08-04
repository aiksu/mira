from django.contrib import admin

# Register your models here.
from core.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user_full_name', 'answer1', 'answer2', 'answer3')
    list_filter = ('user',)

    def upper_case_name(self, obj):
        return obj.user

    upper_case_name.short_description = 'Name'

    def user_full_name(self, obj):
        return '{}({})'.format(obj.user.get_full_name(), obj.user)

    user_full_name.short_description = 'Имя Фамилия'