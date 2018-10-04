from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect('UserPage_home')
    else:
        return render(request, 'PATracker/welcome.html')