from django.contrib import admin
from .models import Page  # importamos de models page

# Register your models here.
class PageAdmin(admin.ModelAdmin):    
     readonly_fields = ('created', 'updated')
     list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)

