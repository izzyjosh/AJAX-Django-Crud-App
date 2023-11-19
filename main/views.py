from django.shortcuts import render
from .forms import PersonInfoForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PersonInfo

@csrf_exempt
def create(request):
    if request.method == "POST":
        form = PersonInfoForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            department = request.POST.get("department")
            course = request.POST.get("course")


            PersonInfo.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    department=department,
                    course=course,)

            person = PersonInfo.objects.values()
            person_data = list(person)

            return JsonResponse({"status":"saved","person_data":person_data})
        else:
            return JsonResponse({"status":"not saved"})


def home(request):
    form = PersonInfoForm()
    persons = PersonInfo.objects.all()
    return render(request,"crud.html",{"form":form,"persons":persons})
