from django.contrib import admin

from API.models import IntelForScienceWorks, TypesOfWork, AuthorNames

# Register your models here.

admin.site.register(IntelForScienceWorks)

admin.site.register(TypesOfWork)

admin.site.register(AuthorNames)