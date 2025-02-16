from django.shortcuts import redirect, render, get_object_or_404
from django.http import FileResponse, Http404
from django.contrib.auth import get_user_model
from .models import *
from .forms import ResumeForm

# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    users = User.objects.all()
    about_data = About.objects.all()  # Fetch all About details
    tech_stack = TechStack.objects.all()  # Fetch tech stack data
    return render(request, "about.html", {"users": users,"about_data": about_data, "tech_stack": tech_stack})
   


def projects (request):
    pr = Project.objects.all()
    return render (request,"projects.html",{"pr" : pr})


def experience(request):
    experience=[
        {"company":"CodSoft",
         "position":"Data Science Intern"},
        {"company":"Alpha Intern",
         "position":"Data Science Intern"},
        
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render (request, "certificate.html")


def contact(request):
    return render (request,"contact.html")
    
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  # Assign logged-in user
            resume.save()
            return redirect('resume')  # Redirect to the resume list page
    else:
        form = ResumeForm()
    
    return render(request, 'upload_resume.html', {'form': form})

def download_resume(request, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id, user=request.user)
        return FileResponse(resume.resume_file.open('rb'), as_attachment=True, filename=resume.resume_file.name)
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
    
User = get_user_model()

def resume_list(request):
    user_id = request.GET.get('user')

    if user_id:
        user_instance = get_object_or_404(User, id=user_id) 
        resumes = Resume.objects.filter(user=user_instance) 
    else:
        resumes = Resume.objects.all()

    return render(request, "resume_list.html", {"resumes": resumes})