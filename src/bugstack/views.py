from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q


from .models import Bug
from .forms import BugForm
from .utils import get_page_indices

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def create_bug(request):
    if request.method == "POST":
        form = BugForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = BugForm()
            messages.success(request, ("The bug was added successfully."))
            return redirect('create-bug')
        else:
            messages.error(request, ("The bug was not added"))
            return render(request, 'bugstack/add_bugs.html', {})
    return render(request, 'bugstack/add_bugs.html', {})

def all_bugs(request):
    bugs = Bug.objects.all().order_by('-time_created')
    context = {
        'bugs': bugs
    }
    
    return render(request, 'bugstack/bugs.html', context)

def all_dead_bugs(request):
    bugs = Bug.objects.filter(is_active=False)
    return render(request, 'bugstack/dead_bugs.html', {'bugs': bugs} )

def search_all_bugs(request):
    q = request.GET.get('q')
    if q:
        query = Bug.objects.distinct().filter(
            Q(name__icontains=q) | 
            Q(error_message__icontains=q) | 
            Q(description__icontains=q) |
            Q(description__icontains=q) |
            Q(project__name__icontains=q) |
            Q(project__description__icontains=q) 
            )

        paginator = Paginator(query, 5)
        page_number = request.GET.get('page', 1)
        bugs_page = paginator.get_page(page_number)
        
        l, r = get_page_indices(page_number, paginator)
        custom_range = range(l, r)   

        context = {
        'q' : q,
        'count': paginator.count,
        'bugs_page': bugs_page, 
        'custom_range': custom_range
        }

        return render(request, 'bugstack/bugs.html', context)
    else:
        return render(request, 'bugstack/bugs.html', {})

def squash_bug(request, bug_id):
    bug = Bug(pk=bug_id)
    bug.is_active = 'False'
    bug.save()
    #if request.user.id == venue.owner:
    #    venue.delete()
    # only venue's owner is authorised to delete venue
    messages.success(request, ("Bug's been squashed."))
    return redirect('list-bugs') # will this redirect to the current page being viewed or page one?
    #else:
    #    messages.success(request, ("This isn't your bug to squash."))
    #    return redirect('list-bugs')



