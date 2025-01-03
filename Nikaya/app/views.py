from django.shortcuts import render
from .forms import CustomUserCreationForm

def register(request):
    if request.method=='POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form= CustomUserCreationForm()
    return render(request,'/home/pranavanand/NikayaLM/Nikaya/app/templates/register.html',{'form':form})

def homepage(request):
    return render(request,'/home/pranavanand/NikayaLM/Nikaya/app/templates/homepage.html')
