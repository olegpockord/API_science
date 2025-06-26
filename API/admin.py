from django.contrib import admin

from API.models import IntelForScienceWorks, TypesOfWork, AuthorNames

# Register your models here.

# admin.site.register(IntelForScienceWorks)

admin.site.register(TypesOfWork)

admin.site.register(AuthorNames)


@admin.register(IntelForScienceWorks)
class AdminIntelForScienceWorks(admin.ModelAdmin):
    list_display = ["title", "authors", "type_of_work",]
    search_fields = ["title", "pk",]
    fields = (
        "title",
        "annotation",
        "OECD",
        "key_words",
        "year_publication",
        "work_type_name",
        ("type_of_work", "authors"),
    )
