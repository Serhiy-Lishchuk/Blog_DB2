from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
from .models import Reg
# Create your views here.


def registration(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        try:
            User.objects.get(username=request.POST.get('username'))
            args['Error'] = 'Under such user name is already registered!'
            return render_to_response('registration.html', args)
        except User.DoesNotExist:
            user = User.objects.create(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email')
            )
            user.save()
            reg_user = Reg.objects.create(
                fullname=request.POST.get('fullname'),
                birthday=request.POST.get('birthday'),
                country=request.POST.get('country'),
                city=request.POST.get('city')
            )
            reg_user.save()
            args['Success'] = 'User created!'
            return render_to_response('registration.html', args)
    else:
        args['Error'] = 'Bad request!'
        return render_to_response('registration.html', args)


def login_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        args['Error'] = False
        if user is not None:
            login(request, user)
            args['user'] = user
            return redirect('base.html', args)
        else:
            args['Error'] = True
            args['MSG'] = 'Invalid login or password!'
            return render_to_response(args)
    else:
        args['Error'] = True
        args['MSG'] = 'Bad request'
        return render_to_response('login.html', args)


def logout_user(request):
    logout(request)
    return redirect('login.html')
