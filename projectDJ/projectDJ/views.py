from django.http import HttpResponse
from django.shortcuts import render
from software.models import Software
from hardware.models import Hardware
from Employee.models import Employees
def homePage(req):
    # data={
    #     'title':'Welcome to Home Page!!',
    #     'clist':['java','c','c++'],
    #     'numb':[10,20,30,40,50,100],
    #     'stud':[{'name':'anurag','phone':'8259038539'},
    #             {'name':'rohit','phone':'1234567891'}
    #             ]
    # }
    if req.method== 'POST':
        id=req.POST['assetId']
        name = req.POST['hardwareName']
        new_block=Hardware(asset_id=id,hardware_name=name)
        new_block.saver()
    edata=Employees.objects.all()
    hdata=Hardware.objects.all()
    sdata=Software.objects.all()
    data={
        'sdata':sdata,
        'hdata':hdata,
        'edata':edata
    }
    return render(req,"index.html",data)
def HomePage(req):
    if req.method== 'POST':
        id=req.POST['assetId']
        name = req.POST['hardwareName']
        new_block=Hardware(asset_id=id,hardware_name=name)
        new_block.saver()
def SoftwarePage(req):
    hdata=Hardware.objects.all()
    sdata=Software.objects.all()
    data={
        'sdata':sdata,
        'hdata':hdata
    }
    return render(req,"software.html",data)
def aboutUs(req):
    return HttpResponse("Welcome to my webpage1!")
def course(req):
    return HttpResponse("Welcome to my webpage2!")

def courseDetails(req,courseid):
    return HttpResponse(courseid)
