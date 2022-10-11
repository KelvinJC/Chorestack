from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone


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
    else:
        form = BugForm
    return render(request, 'bugstack/add_bugs.html', {'form': form})

def all_bugs(request):
    query = Bug.objects.filter(is_active=True).order_by('-time_reported')
    
    paginator = Paginator(query, 5)
    page_number = request.GET.get('page', 1)
    bugs_page = paginator.get_page(page_number)
    
    nums = "a" * bugs_page.paginator.num_pages
    context = {
    'count': paginator.count,
    'bugs_page': bugs_page, 
    'nums': nums
    }
    
    return render(request, 'bugstack/list_bugs.html', context)

def all_dead_bugs(request):
    query = Bug.objects.filter(is_active=False).order_by('-time_resolved')
    paginator = Paginator(query, 5)
    page_number = request.GET.get('page', 1)
    bugs_page = paginator.get_page(page_number)
    
    l, r = get_page_indices(page_number, paginator)
    custom_range = range(l, r)   

    context = {
    'count': paginator.count,
    'bugs_page': bugs_page, 
    'custom_range': custom_range
    }    
    
    return render(request, 'bugstack/dead_bugs.html', context )

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

        return render(request, 'bugstack/search_bugs.html', context)
    else:
        return redirect('list-bugs')

def squash_bug(request, bug_id):
        bug = Bug.objects.get(pk=bug_id)
        bug.is_active = False
        bug.time_resolved = timezone.now()
        bug.save(update_fields=['is_active', 'time_resolved'])
        #if request.user.id == bug.owner:
        #    bug.delete()
        # only bug's owner is authorised to squash bug
        messages.success(request, ("The {} bug has been squashed.".format(bug.name)))
        return redirect('list-bugs') # will this redirect to the current page being viewed or page one?. Ans: It goes to page one
        #else:
        #    messages.success(request, ("This isn't your bug to squash."))
        #    return redirect('list-bugs')

        # hack to get the current page to load
        #return render('bugstack/list_bugs.html/?page={}'.format(num), {})

def update_bug(request, bug_id):
    bug = Bug.objects.get(pk=bug_id)
    form = BugForm(request.POST or None, instance=bug)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = BugForm
            messages.success(request, ("The bug has been updated"))
            return redirect('list-bugs')
        else:
            messages.error(request, ("There's an error with the form"))


    return render(request, 'bugstack/update_bug.html', {'bug': bug, 'form': form})