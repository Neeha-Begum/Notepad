from django.shortcuts import render
from Notes.models import Note
# Create your views here.
def func1(request):
    if request.method=="POST":
        a=request.POST.get('title')
        b=request.POST.get('description')
        obj=Note(title=a, description=b)
        obj.save()
        result=Note.objects.all()
        return render(request,'index.html',{'res':result})
    return render(request,'index.html')