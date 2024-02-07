from django.shortcuts import render
from books.models import Book
from django.db.models import Q

from books.forms import Bookform
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')

def bookdetail(request,p):
    b=Book.objects.get(id=p)
    return render(request,'book.html',{'b':b})
@login_required
def bookdelete(request,p):
    b = Book.objects.get(id=p)
    b.delete()
    return viewbooks(request)
@login_required
def bookedit(request,p):
    if (request.method == "POST"):
        form=Bookform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return viewbooks(request)
    b = Book.objects.get(id=p)
    form=Bookform(instance=b)
    return render(request,'edit.html',{'form':form})
@login_required
def search(request):
    query=" "
    b=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            b=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request,'search.html',{'query':query,'b':b})

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save
        return viewbooks(request)
    return render(request,'addbook.html')

@login_required
def addbooks1(request):
    if (request.method=="POST"):     #aftr form submission
        form=Bookform(request.POST)  #creates form object initialised with values inside request.POST
        if form.is_valid():
            form.save()              # saves the form object inside Db table
        return viewbooks(request)


    form=Bookform()  #  creates empty form object WITH NO VALUES
    return render(request,'addbooks1.html',{'form':form})
@login_required
def viewbooks(request):
    k=Book.objects.all()

    return render(request,'viewbook.html',{'b':k})
@login_required
def fact(request):
    if(request.method=="POST"):
        num=int(request.POST['n'])
        f=1
        for i in range(1,num+1):
            f=f*i

            return render(request, 'fact.html',{'fact':f})

    return render(request,'fact.html')
