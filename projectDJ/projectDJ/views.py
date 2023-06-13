from django.http import HttpResponse
from django.shortcuts import render
from software.models import Software
from hardware.models import Hardware

def homePage(req):
    # data={
    #     'title':'Welcome to Home Page!!',
    #     'clist':['java','c','c++'],
    #     'numb':[10,20,30,40,50,100],
    #     'stud':[{'name':'anurag','phone':'8259038539'},
    #             {'name':'rohit','phone':'1234567891'}
    #             ]
    # }
    hdata=Hardware.objects.all()
    sdata=Software.objects.all()
    data={
        'sdata':sdata,
        'hdata':hdata
    }
    return render(req,"index.html",data)
def aboutUs(req):
    return HttpResponse("Welcome to my webpage1!")
def course(req):
    return HttpResponse("Welcome to my webpage2!")

def courseDetails(req,courseid):
    return HttpResponse(courseid)