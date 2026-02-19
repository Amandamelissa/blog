from django.contrib import admin

from .models import PostModel , Category

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    ...

class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)
