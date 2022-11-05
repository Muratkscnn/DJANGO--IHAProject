from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import ihacat


def home(request):
    iha = ihacat.objects.all()
    if request.method == "POST":
        brand = request.POST["search"]
        iha = ihacat.objects.filter(brand=brand)
    return render(request, "home.html", {"ihalist": iha})


@login_required
def ihalist(request):
    iha = ihacat.objects.all()
    if request.method == "POST":
        id = request.POST["id"]
        object = ihacat.objects.get(pk=id)
        object.delete()
    return render(request, "ihalist.html", {"ihalist": iha})


def detail(request, id):
    print(id)
    iha = ihacat.objects.get(pk=id)
    return render(request, "detail.html", {"iha": iha})

@login_required
def create(request):
    if request.method == "POST":
        modelname = request.POST["modelname"]
        brand = request.POST["brand"]
        img = request.POST["img"]
        weight = request.POST["weight"]
        categories = request.POST["categories"]
        description = request.POST["description"]
        object = ihacat()
        object.modelname = modelname
        object.brand = brand
        object.weight = weight
        object.categories = categories
        object.img = img
        object.description = description
        object.save()
        return render(request,"create.html",{"statuscode":"succes"})
    return render(request,"create.html",{})

@login_required
def edit(request, id):
    iha = ihacat.objects.get(pk=id)
    if request.method == "POST":
        if "modelname" in request.POST:
            id = request.POST["id"]
            modelname = request.POST["modelname"]
            brand = request.POST["brand"]
            img = request.POST["img"]
            categories = request.POST["categories"]
            description = request.POST["description"]
            object = ihacat.objects.get(pk=id)
            object.modelname = modelname
            object.categories = categories
            object.brand = brand
            object.img = img
            object.description = description
            object.save()
            return render(request,"edit.html",{"iha":object})
        else:
            # elif request.method == "POST":
            id = request.POST["id"]
            object = ihacat.objects.get(pk=id)
            object.delete()

    return render(request, "edit.html", {"iha": iha})



