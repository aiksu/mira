from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Answer(models.Model):
    user = models.ForeignKey(User, verbose_name='О ком ответ', on_delete=models.CASCADE, related_name='answer_results')
    answer1 = models.TextField(verbose_name='Первый')
    answer2 = models.TextField(verbose_name='Второй')
    answer3 = models.TextField(verbose_name='Третий')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('core:answer-success', kwargs={'user_id': self.user.id})


class Poll(models.Model):
    user = models.ForeignKey(User, verbose_name='О ком ответ', on_delete=models.CASCADE, related_name='poll_results')
    poll1 = models.TextField(verbose_name='Если бы вы были в комнате, где меня нет, как бы вы описали меня другому человеку? Что бы вы сказали обо мне?')
    poll2 = models.TextField(verbose_name='Как вы думаете в чем я хорошо разбираюсь? В какой сфере вы попросили бы мой совет?')
    poll3 = models.TextField(verbose_name='Предположите, какой у меня уровень дохода?')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('core:poll-success', kwargs={'user_id': self.user.id})
