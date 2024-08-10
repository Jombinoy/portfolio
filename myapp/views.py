from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def Academic(request):
    return render(request, 'Academic.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')




# myapp/views.py
from django.shortcuts import render, redirect
from .forms import HireMeForm

def hire_me_view(request):
    if request.method == 'POST':
        form = HireMeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or home page
    else:
        form = HireMeForm()
    return render(request, 'hire_me_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')

from django.shortcuts import render
from django.conf import settings
from django.templatetags.static import static

def resume_page_view(request):
    resume_url = static('resumes/JOM_BINOY.pdf')  # Adjust the path if needed
    return render(request, 'resume_page.html', {'resume_url': resume_url})
