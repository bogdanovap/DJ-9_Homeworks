from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Tag, ArticleTags

class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        tags = []
        has_main = False
        for form in self.forms:
            print("")
            print("")
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            tags.append(form.cleaned_data.get("tag"))
            if form.cleaned_data.get("is_main") == True:
                if has_main == False:
                    has_main = True
                else: 
                    raise ValidationError('Основным может быть только один раздел')

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            #raise ValidationError('Тут всегда ошибка')
        
        if (len(tags) == 0):
            raise ValidationError('Должен быть указан хотя бы один раздел')

        if (has_main == False):
            raise ValidationError('Необходимо указать основной раздел')

            
        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ArticleTagsInline]


