from django.contrib import admin
from .models import Link  # importamos de models Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):    
     readonly_fields = ('created', 'updated')

     def get_readonly_fields(self, request, obj=None):  # esto es para que el usario no pueda                                                        # cambiar los datos
          if request.user.groups.filter(name="Personal").exists():
               return ('key', 'name')
          else:
                return ('created', 'updated')

admin.site.register(Link, LinkAdmin)  # activamos en el admin.site.register el Link y el LinkAdmin
