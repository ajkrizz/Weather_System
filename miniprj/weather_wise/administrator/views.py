from django.http import HttpResponse
from django.template import loader
from .forms import UserCreationForm
from django.shortcuts import render, redirect


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request, 'user_creation.html', {'form': form})
  
