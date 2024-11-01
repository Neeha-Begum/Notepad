from django.shortcuts import render
from Contacts.models import List
# Create your views here.
def func1(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('contact')
        obj=List(name=a, contact=b)
        obj.save()
        result=List.objects.all()
        return render(request,'contact.html',{'res':result})
    return render(request,'contact.html')

def func2(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('contact')
        obj=List.objects.get(name=a)
        obj.contact=b
        obj.save()
        result=List.objects.all()
        return render(request,'contact.html',{'res':result})
    return render(request,'contact.html')