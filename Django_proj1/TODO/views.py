from django.shortcuts import render
#Create your views here.
from django.http.response import HttpResponse

def index(request):
    return HttpResponse('Hello')

tasks = [
        {'id': 1, 'content': 'lorem', 'priority': 1, 'desc': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"},
        {'id': 2, 'content': 'lorem2', 'priority': 2, 'desc': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"},
        {'id': 3, 'content': 'lorem3', 'priority': 3, 'desc': 'lorem lorem'},
        {'id': 4, 'content': 'lorem3', 'priority': 5, 'desc': 'lorem lorem'},
        {'id': 5, 'content': 'lorem3', 'priority': 4, 'desc': 'lorem lorem'},
        {'id': 6, 'content': 'lorem3', 'priority': 5, 'desc': 'lorem lorem'},
    ]
def list(request):

    return render(request,template_name="todo_list.html",context={'data':tasks}) #alias of tasks for sending data

def view_data(request,list_id,*args):
    print(request.GET)
    list_ID= int(list_id)
    obj1=0
    for i in tasks :
        if list_ID==i.get('id'):

            obj1=i

    return render(request,template_name="view_data.html",context={'record':obj1})

def update(request,list_id):
    list_ID = int(list_id)
    obj1 = 0
    for i in tasks:
        if list_ID == i.get('id'):
            i['content']+='updated'
            obj1 = i

    return render(request, template_name="view_data.html", context={'record': obj1})

def delete(request,list_id):
    list_ID = int(list_id)
    obj1 = 0
    for i in tasks:
        if list_ID == i.get('id'):
            tasks.remove(i)

    return render(request, template_name="todo_list.html", context={'data': tasks})

def insert(request):
    record={'id': 100, 'content': 'lorem100', 'priority': 2, 'desc': 'lorem lorem lorem'}
    tasks.append(record)
    return render(request, template_name="todo_list.html", context={'data': tasks})
