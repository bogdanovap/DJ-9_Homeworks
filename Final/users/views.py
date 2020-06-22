from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignupForm
from .models import User


# Create your views here.
def signup(request):
    template_name = 'registration\\signup.html'
    form = SignupForm
    context = {
        "form": form
    }

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                email=form.cleaned_data.get('email'),
            )
            login(request, User.objects.get(email=form.cleaned_data.get('email')))
            return redirect("index")
        else:
            context['form'] = form
            return render(request=request,
                          template_name=template_name,
                          context=context)

    return render(request, template_name, context)
