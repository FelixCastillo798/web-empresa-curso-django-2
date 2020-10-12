from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin (admin.ModelAdmin):
     readonly_fields = ('created', 'updated')

class PostAdmin (admin.ModelAdmin):
     readonly_fields = ('created', 'updated')
     list_display = ('title', 'author', 'published', 'post_categories') # Mostrar columnas
     ordering = ('author', 'published')
     search_fields = ('title', 'content', 'author__username', 'categories__name')
     date_hierarchy = ('published')
     list_filter = ('author__username', 'categories__name') # Filtrar por varios campos

     def post_categories(self, obj): # Filtrar campos con relacion many to many
          return ", ".join([c.name for c in obj.categories.all().order_by("name")])
     post_categories.short_description = "Categorías"  # esto pone el nombre de la columna

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)




