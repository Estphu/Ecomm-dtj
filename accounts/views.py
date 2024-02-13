from django.shortcuts import render
from django.http import HttpRequest
from .forms import SignUpForm 

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpRequest("Done!")
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})    