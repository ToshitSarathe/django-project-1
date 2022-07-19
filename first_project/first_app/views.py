from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
# Create your views here.


def index(request):
    #return HttpResponse("<em>Hello World!!This is my homePage</em>")
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request,"first_app/index.html",context = date_dict)
def about(request):
    return HttpResponse("<em>This is about page!!</em>")

def contacts(request):
    return HttpResponse("<em>This is contacts page!!</em>")

def services(request):
    return HttpResponse("<em>This is services page</em>")
