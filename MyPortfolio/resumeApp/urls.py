
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("experience/", views.experience, name="experience"),
    path("certificate/", views.certificate ,name="certificate"),
    path("contact/", views.contact, name="contact"),
    path('resume/', views.upload_resume, name='resume_upload'),
    path('resume-list/', views.resume_list, name='resume'),
    path('resume/download/<int:resume_id>/', views.download_resume, name='download_resume')

]