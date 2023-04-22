from django.shortcuts import render, redirect
from .models import MyUser
from .forms import MyUserForm
# Create your views here.

message = ''
login_user = ''

def home(request):
    return render(request, 'main/home.html', context={'login_user':login_user})


def login(request):
    global message, login_user
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        name = request.POST.get('user_name')
        password = request.POST.get('user_password')
        my_user = MyUser.objects.all()
        for i in my_user:
            if i.user_name == name and i.user_password == password:
                login_user = name
                return redirect('home')
        else:
            message = 'Invalid name or password'
            return redirect('login')
    else:
        form = MyUserForm()
    return render(request, 'main/login.html', context={
        'form':form,
        'message':message
    })


def register(request):
    chars = '!@#$%^&*()'
    char_count = 0
    number_count = 0
    let_count = 0
    global message
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        name = request.POST.get('user_name')
        password = request.POST.get('user_password')
        if len(password) < 8:
            message = 'Invalid Password'
            return redirect('register')
        else:
            if password[0].isupper():
                for i in password:
                    if i.isdigit():
                        number_count += 1
                    elif i in chars:
                        char_count += 1
                    else:
                        let_count += 1
                if number_count >= 1 and char_count >= 1 and let_count >= 6:
                    message = ''
                    MyUser.objects.create(user_name=name, user_password=password)
                    return redirect('login')
                else:
                    message = 'Invalid Password'
                    return redirect('register')
            else:
                message = 'Invalid Password'
                return redirect('register')
    else:
        form = MyUserForm()
    return render(request, 'main/signup.html', context={
        'form':form,
        'message':message
    })


def logout(request):
    global login_user
    login_user = ''
    return redirect('home')



# message = 'Hello Tiko'