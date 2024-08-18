from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


"""сообщаем сайту администрирования, что модель зарегистрирована на 
сайте с использованием конкретно-прикладного класса, который наследует 
от ModelAdmin. В этот класс можно вставлять информацию о том, как показывать
модель на сайте и как с ней взаимодействовать.
Атрибут list_display позволяет задавать поля модели, которые вы хотите 
показывать на странице списка объектов администрирования. Декоратор 
@admin.register() выполняет ту же функцию, что и функция admin.site.register(), 
которую вы заменили, регистрируя декорируемый им класс ModelAdmin."""
