from django.contrib import admin
from .models import CountryModel, LanguagesModel


class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "country")


class LanguagesAdmin(admin.ModelAdmin):
    list_display = ("id", "languages")


admin.site.register(CountryModel, CountryAdmin)
admin.site.register(LanguagesModel, LanguagesAdmin)
