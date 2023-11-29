from django.shortcuts import render
from catalog.models import Category
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'
    
index = IndexView.as_view()
      
  
def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            success = True
            form = ContactForm()
        else:
            messages.error(request, 'Formulário Inválido')

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
