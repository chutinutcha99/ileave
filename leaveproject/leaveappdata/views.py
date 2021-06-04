from leaveproject import leaveappdata
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'leaveappdata/home.html')
