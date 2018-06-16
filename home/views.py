from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from django.contrib import auth
from home.models import  Item,User
from home.forms import SignupForm, ItemForm

import datetime
import time


def handle_uploaded_file(f,name):
    ext=str(name.split(".").pop())
    name=str(time.time()).replace(".","")
    filename='media/media/'+name+"."+ext
    fname="/media/"+name+"."+ext
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return fname

def index(request):
    if request.session.get('user',None):
        items=Item.objects.all()
        user=User.objects.get(emailId=request.session.get('user'))
        return render(request,'home/home.html',{"items":items,"user":user})
    else:

       return HttpResponseRedirect('/login')

def help(request):
    return render(request,'home/help.html',{})



def logout(request):
      del request.session['user']
      return HttpResponseRedirect('/home')



def signup(request):
    msg=""
    if request.POST:
        try:
           user=SignupForm(request.POST)
           user.save()
           request.session['user']=request.POST.get('emailId')
           return HttpResponseRedirect('/home')
        except Exception,e:
            msg=e
            print e
    signupform = SignupForm()
    return render(request,'home/signup.html',{"signupform":signupform,"msg":msg})

def login(request):
    error=""
    if request.POST:
     data=request.POST
     emailId=data.get('username')
     password=data.get('password')
     flag=False
     try:
          user=User.objects.get(emailId=emailId)
          if user.emailId==emailId and user.password==password :
               flag=True
               request.session['user']=emailId
               return HttpResponseRedirect('/home')
          else:
               flag=False
     except Exception,e:
          error=e
    return render(request,'home/login.html',{"error":error})


def myitem(request):
     if request.POST:
         if request.POST.get('deleteItem',None):
            try:
               id=request.POST.get("itemId")
               item=Item.objects.get(id=id)
               user=User.objects.get(emailId=request.session.get('user'))
               if item.user == user :
                   item.delete()
               else:
                   print "nice try"
            except:
               print "something wrong"
         return HttpResponseRedirect('/myitem')

     user=User.objects.get(emailId=request.session.get('user'))
     items=user.item_set.all()
     print items
     return render(request,'home/myitem.html',{"items":items})

def additem(request):
    if request.POST:
         f=request.FILES.get('image')
         name=f.name
         filename=handle_uploaded_file(f,name)
         newItem=Item()
         newItem.name=request.POST.get('name')
         newItem.price=request.POST.get('price')
         newItem.info=request.POST.get('info')
         newItem.status="available"
         newItem.image=filename
         newItem.user=User.objects.get(emailId=request.session.get('user'))
         newItem.save()


    itemform = ItemForm()
    return render(request,'home/additem.html',{"itemform":itemform})
