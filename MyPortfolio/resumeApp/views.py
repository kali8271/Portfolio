from django.shortcuts import redirect, render, get_object_or_404
from django.http import FileResponse, Http404
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import *
from .forms import ResumeForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django import forms
from django.contrib.syndication.views import Feed

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
    if request.method == 'POST':
        if request.POST.get('website'):
            # Honeypot field filled: likely spam
            messages.error(request, 'Spam detected. Submission ignored.')
            return redirect('contact')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if name and email and message:
            full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
            send_mail(
                subject=f"Portfolio Contact Form: {name}",
                message=full_message,
                from_email=None,  # Uses DEFAULT_FROM_EMAIL
                recipient_list=['akalimuallah900@gmail.com'],
            )
            messages.success(request, 'Thank you for contacting me! I will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
    return render(request, "contact.html")
    
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
    # user_id = request.GET.get('user')

    # if user_id:
    #     user_instance = get_object_or_404(User, id=user_id) 
    #     resumes = Resume.objects.filter(user=user_instance) 
    # else:
    #     resumes = Resume.objects.all()

    resumes = Resume.objects.all()
    print("Resumes Retrieved:", resumes)
    return render(request, "resume.html", {"resumes": resumes})

def blog_list(request):
    posts = BlogPost.objects.order_by('-date_posted')
    return render(request, 'blog_list.html', {'posts': posts})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']

def blog_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    comments = post.comments.order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('blog_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'form': form})

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    def items(self):
        return BlogPost.objects.all()
    def lastmod(self, obj):
        return obj.date_posted
    def location(self, obj):
        return f"/blog/{obj.id}/"

class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'
    def items(self):
        return ['home', 'about', 'experience', 'certificate', 'contact', 'blog_list']
    def location(self, item):
        return reverse(item)

class BlogFeed(Feed):
    title = "Kalimullah Ansari Blog"
    link = "/blog/"
    description = "Latest blog posts from Kalimullah Ansari."
    def items(self):
        return BlogPost.objects.order_by('-date_posted')[:10]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content
    def item_link(self, item):
        return f"/blog/{item.id}/"

def testimonials(request):
    testimonials = Testimonial.objects.order_by('-created_at')
    return render(request, 'testimonials.html', {'testimonials': testimonials})