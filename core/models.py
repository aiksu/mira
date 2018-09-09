from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Answer(models.Model):
    user = models.ForeignKey(User, verbose_name='О ком ответ', on_delete=models.CASCADE, related_name='answers')
    answer1 = models.TextField(verbose_name='Первый')
    answer2 = models.TextField(verbose_name='Второй')
    answer3 = models.TextField(verbose_name='Третий')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('core:answer-success', kwargs={'user_id': self.user.id})



