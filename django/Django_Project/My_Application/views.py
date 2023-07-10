from django.shortcuts import render
from .models import register

def registerpage(request):
    if request.method == 'POST':
        getname = request.POST.get('name')
        getaddress = request.POST.get('address')
        getusername = request.POST.get('username')
        getpassword = request.POST.get('password')
        users = register()
        users.Name = getname
        users.Address =getaddress
        users.password = getpassword
        users.save()

    return render(request,'registerpage.html',{})

