from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project, Message
from .forms import ContactForm

# Create your views here.
def index(request):
    projects = Project.objects
    return render(request, 'portfolio/index.html', {'projects':projects})


def about(request):
    return render(request, 'portfolio/about.html')

def works(request):
    projects_1 = Project.objects.all()[:3]
    projects_2 = Project.objects.all()[3:]

    return render(request, 'portfolio/works.html', {'projects_1':projects_1, 'projects_2':projects_2})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'portfolio/thankyou.html')
        # else:
        #     form = ContactForm()
        #     return render(request, 'portfolio/contact.html', {'form':form})
    else:
        form = ContactForm()
        return render(request, 'portfolio/contact.html', {'form': form})


def thankyou(request):
    return render(request,'portfolio/contact.html')