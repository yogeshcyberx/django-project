from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import User
from pyresparser import ResumeParser
import warnings
 
warnings.filterwarnings("ignore", category=UserWarning)

# Create your views here.
def index(request):
    print('function called')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if request.POST.get('phone') == '':
            phone = None
        else:
            phone = request.POST.get('phone')
        resume = request.FILES.get('resume')

        saveForm = User(name=name, email=email, contact_number=phone, file=resume)
        saveForm.save()

        saved_instance = User.objects.get(id=saveForm.id)
        getName = saved_instance.file.name  # Get name of the saved record
        getResume = saved_instance.file.path  # Get path to the saved resume file
        print(getResume)
        # return HttpResponse(getName)
        # return HttpResponse(getResume)
        data = ResumeParser(getResume).get_extracted_data()
        print("Email:", data["email"])
        return redirect('/')

    return render(request, "resume.html")