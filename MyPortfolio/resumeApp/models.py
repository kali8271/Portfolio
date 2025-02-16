from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self) -> str:
        return self.name  # Updated to return the name instead of about


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='about')
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self) -> str:
        return f"About {self.user.name}"

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tech_stack/')

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField(default='http://default.url.com')

    def __str__(self) -> str:
        return self.title


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    resume_file = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.resume_file.name}"