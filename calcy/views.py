from django

def home(request):
    return render(request, 'home.html')