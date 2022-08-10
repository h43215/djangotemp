from django.shortcuts import render,redirect
from .models import Contact

def contact(request):
    return render(request,"contact/contact.html")

def viewcontact(request):
    s = Contact.objects.all()
    return render(request,"contact/viewcontact.html",{"data":s})

def Editcontact(request):
    s = Contact.objects.get(pk=request.GET["q"])
    return render(request,"contact/editcontact.html",{"data":s})

def Edit(request):
    email = request.POST.get("text_mail")  
    mobile = request.POST.get("text_mob")  
    message = request.POST.get("text_massage")
    s= Contact.objects.get(pk=request.POST.get("text_id"))
    s.email = email
    s.massage = message
    s.mobile = mobile
    s.save()
    s = Contact.objects.all()
    return render(request,"contact/viewcontact.html",{"data":s})

def Deletecontact(request):
    s = Contact.objects.get(pk=request.GET["q"]) 
    s.delete()
    s = Contact.objects.all()
    return render(request,"contact/viewcontact.html",{"data":s})   

def contactcode(request):    
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    message = request.POST.get('message')
    obj = Contact(email=email,mobile= mobile,massage=message)
    obj.save()
    return redirect('viewcontact')
    