from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def delete_booking(request):
    return render(request, "index.html")

@login_required
def edit_booking(request):
    return render(request, "index.html")

