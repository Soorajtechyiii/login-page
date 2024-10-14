from django.shortcuts import render #type:ignore
from django.template import loader#type:ignore
from django.http import HttpResponse#type:ignore
from myapp.models import user
def pagehtml(request):
    id=loader.get_template('demo1html.html')
    return HttpResponse(id.render())
def fsave(request):
    if request.method =='POST':
        username=request.POST.get('USERNAME')
        email=request.POST.get('EMAIL')
        password=request.POST.get('PASSWORD')
        u=user(username=username,email=email,password=password)
        u.save()
        u=user.objects.all()
        return render(request,'displaydata.html',{'user':user})
    else:
        return HttpResponse('data not saved')
def login(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        mail=request.POST.get('mail2')
        pwd=request.POST.get('pwd')
        log=user.objects.filter(username=uname,email=mail,password=pwd)
        if(len(log)>0):
            return HttpResponse('data saved')
        else:
            return HttpResponse('data not saved')

    
        
    
       
       
       




