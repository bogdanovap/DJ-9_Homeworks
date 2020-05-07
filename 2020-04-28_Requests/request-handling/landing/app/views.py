from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()

land_pages = {'original':'landing.html', 'test':'landing_alternate.html'}

def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing

    param_name='from-landing'
    
    land_type = request.GET.get(param_name,'none')
    counter_click[land_type] += 1

    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    param_name='ab-test-arg'

    land_type = request.GET.get(param_name,'none')
    counter_show[land_type]+=1
    
    page_to_render = land_pages.get(land_type,'landing.html')

    return render_to_response(page_to_render)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': counter_click['test']/counter_show['test'] if counter_show['test'] else 0,
        'original_conversion': counter_click['original']/counter_show['original'] if counter_show['original'] else 0,
    })
