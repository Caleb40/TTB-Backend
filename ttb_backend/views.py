from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'ttb_backend/index.html')