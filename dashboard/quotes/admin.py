from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Language, Quote, Translate


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0
    fields = ['code', 'name']
    readonly_fields = ['code', 'name']


class TranslateInline(admin.TabularInline):
    model = Translate
    inlines = [LanguageInline]
    extra = 0
    fields = ['quote', 'text', 'language']


@admin.register(Quote)
class QuoteAdmin(ModelAdmin):
    inlines = [TranslateInline]
    list_display = ('original', 'author')
    search_fields = ['original', 'author']


@admin.register(Translate)
class TranslateAdmin(ModelAdmin):
    list_display = ('quote', 'language_tag', 'text')
    search_fields = ['quote', 'language_tag', 'text']

    def language_tag(self, obj):
        return obj.language.name

    language_tag.short_description = 'Language'


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ['code', 'name']
