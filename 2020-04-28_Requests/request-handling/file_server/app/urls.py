from django.urls import path, register_converter
from app.views import file_list, file_content
import datetime

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime.date:
        return datetime.datetime.strptime(value, self.format).date()

    def to_url(self, value: datetime.datetime.date) -> str:
        return value.strftime(self.format)

register_converter(DateConverter, 'date')


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path("", file_list, name='file_list'),    
    # задайте необязательный параметр "date"
    # для детальной информации смотрите HTML-шаблоны в директории templates
    path("<date:date>/", file_list, name='file_list'),
    path("file_content/<str:name>", file_content, name='file_content'),
]
