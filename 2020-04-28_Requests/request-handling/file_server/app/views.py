from django.shortcuts import render
import datetime
from django.conf import settings
from os import listdir, path

def file_list(request, date: datetime.date = None):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_list = []
    for file in listdir(settings.FILES_PATH):
        ctime = datetime.datetime.fromtimestamp(path.getctime(settings.FILES_PATH+"\\"+file))
        mtime = datetime.datetime.fromtimestamp(path.getmtime(settings.FILES_PATH+"\\"+file))
        if date == None:
            file_list.append(
                {'name':file,
                 'ctime':ctime,
                 'mtime':mtime,
                    })
        elif (date == ctime.date() or date == mtime.date()):
            file_list.append(
                {'name':file,
                 'ctime':ctime,
                 'mtime':mtime,
                    })

    context = {
        'files': file_list,
        'date': date if date else None # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_content = []
    with open(settings.FILES_PATH+"\\"+name) as f:
        for line in f:
            file_content.append(line)
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': " ".join(file_content)}
    )

