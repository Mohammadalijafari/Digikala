from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import UserLoginForm


# Create your views here.
def login_view(request):
    if request.method == "GET":
        form = UserLoginForm()

    else:
        form = UserLoginForm(request.POST, request=request)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request=request, user=user)
            return redirect('')

    context = {
        'form': form,

    }
    return render(request, 'accounts/login_view.html', context)
