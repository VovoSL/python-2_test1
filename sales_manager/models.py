from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=124,
        db_index=True,
        verbose_name="Название"
    )
    text = models.TextField(verbose_name="Описание")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    date_publish = models.DateField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Дата публикации"
    )

    # Возвращает название в админке, вместо book1 , 2 и т.д.
    def __str__(self):
        return self.title
