import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from list.models import ToDo, Category

def response(message, status_code):
    response = HttpResponse(message)
    response.status_code = status_code
    return response

def index(request):
    return HttpResponse("Hello, world!")

def list(request):
    to_do_list = ToDo.objects.all().order_by('achieved', "name")
    return render(request, "list/list.html", {'to_do_list': to_do_list})

def addTask(request):
    if request.method == "GET":
        categories = Category.objects.all().order_by('name')
        return render(request, "list/addTask.html", {'categories': categories})
    if request.method == "POST":
        name = request.POST['name']
        category = int(request.POST['category'])
        category = Category.objects.get(id=category)
        if len(name) < 200:
            toDo = ToDo(name=name, category=category, achieved=False)
            toDo.save()
            return redirect('/list')
        else:
            response("Invalid task", 400)

def changeAchieved(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        id = int(data['id'])
        achieved = data['achieved']
        if isinstance(achieved, bool):
            toDo = ToDo.objects.filter(id=id)[0]
            toDo.achieved = achieved
            toDo.save()
            return response('OK', 200)
        else:
            return response('Invalid data type', 400)

def deleteTask(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        id = int(data['id'])
        ToDo.objects.filter(id=id).delete()
        return response('OK', 200)

def editTask(request):
    if request.method == "GET":
        id = int(request.GET['id'])
        categories = Category.objects.all().order_by('name')
        name = ToDo.objects.get(id=id).name
        return render(request, "list/editTask.html", {'categories': categories,
                                                      'name': name,
                                                      'id': id})
    if request.method == "POST":
        id = int(request.GET['id'])
        name = request.POST['name']
        category = request.POST['category']
        if len(name) < 200:
            toDo = ToDo.objects.filter(id=id)[0]
            toDo.name = name
            toDo.category = Category.objects.get(id=category)
            toDo.save()
            return redirect('/list')
        else:
            response("Invalid task", 400)
