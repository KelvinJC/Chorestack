from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Bug
from .forms import BugForm


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def create_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST or None)
        if form.is_valid():
            b = form.cleaned_data 
            Bug.objects.create(
                name = b['name']
            )
            form = BugForm()
            return redirect('list-bugs')
        else:
            messages.error(request, ("The bug was not added"))
            return render(request, 'bugstack/bugs.html', {})
    return render(request, 'bugstack/bugs.html', {})

def all_bugs(request):
    bugs = Bug.objects.all().order_by('-time_created')
    context = {
        'bugs': bugs
    }
    
    return render(request, 'bugstack/bugs.html', context)
