from django.shortcuts import render
from .forms import PersonInfoForm
from django.http import JsonResponse

def create(request):
    if request.method == "POST":
        form = PersonInfoForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({"status":"user saved successfully"})
        else:
            return JsonResponse({"status":"user not saved"})

    else:
        form = PersonInfoForm()

