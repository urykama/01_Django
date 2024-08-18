from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

"""Создание модели поста
Сначала мы определим модель Post, которая позволит хранить посты блога в базе данных."""


class Post(models.Model):
    class Status(models.TextChoices):
        """Добавим в модель поле статуса, которое позволит управлять статусом постов блога.
        В постах будут использоваться статусы Draft (Черновик) и Published (Опубликован)."""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        """Этот класс определяет метаданные модели. Мы используем атрибут ordering, сообщающий Django,
        что он должен сортировать результаты по полю publish."""
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title


"""
• title: поле заголовка поста. Это поле с типом CharField, которое транслируется в столбец VARCHAR в базе данных SQL;
• slug: поле SlugField, которое транслируется в столбец VARCHAR в базе данных SQL. Слаг – это короткая метка, 
    содержащая только буквы, цифры, знаки подчеркивания или дефисы. Пост с заголовком «Django Reinhardt:
    A legend of Jazz» мог бы содержать такой заголовок: «django-reinhardtlegend-jazz». 
    В главе 2 «Усовершенствование блога за счет продвинутых функциональностей» мы будем использовать поле slug для 
    формирования красивых и  дружественных для поисковой оптимизации URLадресов постов блога;
• body: поле для хранения тела поста. Это поле с типом TextField, которое 
    транслируется в столбец Text в базе данных SQL.
     модель Post были добавлены следующие ниже поля:
• publish: поле с типом DateTimeField, которое транслируется в  столбец DATETIME в  базе данных SQL. Оно будет
    использоваться для хранения даты и времени публикации поста. По умолчанию значения поля задаются методом Django
    timezone.now. Обратите внимание, что для того, чтобы использовать этот метод, был импортирован модуль timezone.
    Метод timezone.now возвращает текущую дату/время в формате, зависящем от часового пояса. 
    Его можно трактовать как версию стандартного метода Python datetime.now с учетом часового пояса;
• created: поле с типом DateTimeField. Оно будет использоваться для хранения даты и  времени создания поста.
    При применении параметра auto_now_add дата будет сохраняться автоматически во время создания объекта;
• updated: поле с типом DateTimeField. Оно будет использоваться для хранения последней даты и времени обновления поста.
    При применении параметра auto_now дата будет обновляться автоматически во время сохранения объекта.
    В модельный класс также добавлен метод __str__(). Это метод Python, который применяется по умолчанию
    и возвращает строковый литерал с удобочитаемым представлением объекта. Django будет использовать этот метод
    для отображения имени объекта во многих местах, таких как его сайт администрирования.
"""
"""
post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
"""