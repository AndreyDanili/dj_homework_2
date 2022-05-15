from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopes, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_main = 0
        for form in self.forms:
            tag_info = form.cleaned_data
            if 'is_main' in tag_info.keys():
                if tag_info['is_main']:
                    tag_main += 1
                elif not tag_info['is_main']:
                    continue
        if tag_main == 0:
            raise ValidationError('Выберите основной раздел')
        elif tag_main > 1:
            raise ValidationError('Выберите только один основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scopes
    extra = 2
    ordering = ["-is_main"]
    formset = RelationshipInlineFormset


@admin.register(Article, Tag)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
