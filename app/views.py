from django.shortcuts import render,redirect
from app.models import Note
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages

def home(request):
    return render(request,"home.html")

def createNote(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            note = Note(title=request.POST['title'],description=request.POST['description'],user=request.user)
            note.save()
            messages.success(request,"Note created successfully..")
            return redirect("/my-notes/")
    else:
        context={
            "btn_text":"CREATE"
        }
        return render(request,"create.html",context)

def getAllNotes(request):
    context={
        "heading":"ALL NOTES",
        "notes":Note.objects.all().order_by('-id')
    }
    return render(request,"notes-list.html",context)

def getSingleNote(request,pk):
    context={
        "note":Note.objects.filter(id=pk).first()
    }
    return render(request,"note.html",context)

def updateNote(request,pk):
    note = Note.objects.get(id=pk)
    if request.method == "POST":
        note.title = request.POST.get('title')
        note.description = request.POST.get('description')
        note.save()
        messages.success(request,"Note updated successfully...")
        return redirect("/my-notes/")
        
    context={
        "btn_text":"UPDATE",
        "note":note
    }
    return render(request,"create.html",context)

def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    if request.method =="POST":
        note.delete()
        messages.success(request,"Note delete successfully...")
        return redirect("/my-notes/")
    context={
        "note":note
    }
    return render(request,"delete.html",context)


def getMyNotes(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)
    context={
        "heading":"MY NOTES",
        "notes":notes,
    }
    return render(request,"notes-list.html",context)

def userLogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"User is Login successful!")
            return redirect("/my-notes/")            
        else:
            messages.success(request,"Invalid username or password")
            return redirect("/login/")

    return render(request,"login.html")


def userRegister(request):
    if request.method =="POST":
        check_username = User.objects.filter(username=request.POST['username']).first()
        check_email = User.objects.filter(email=request.POST['email']).first()
        if check_email is not None:
            messages.success(request,"Email is already taken!")
            return redirect("/register/")
        elif check_username is not None:
            messages.success(request,"Username is already taken!")
            return redirect("/register/")
        else:
            user = User.objects.create_user(email=request.POST['email'],first_name=request.POST['fName'],last_name=request.POST['lName'],username=request.POST['username'])

            user.set_password(request.POST['password'])

            user.save()
            messages.success(request,"User created successfully")

            return redirect("/login/")

    return render(request,"register.html")



def userLogout(request):
    logout(request)
    return redirect("/login/")


