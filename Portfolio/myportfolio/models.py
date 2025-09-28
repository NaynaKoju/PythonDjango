from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    
    def __str__(self):
        return self.name


class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"About Section"

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Contact Info"
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # project link

    def __str__(self):
        return self.title

class CV(models.Model):
    title = models.CharField(max_length=200, default="My CV")
    file = models.FileField(upload_to='cv_files/')  # PDF uploads go here
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

