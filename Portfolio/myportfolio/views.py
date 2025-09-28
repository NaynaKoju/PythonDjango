
from django.shortcuts import render
from .models import Project, Skill, Bio, About, Contact, CV

def home(request):
    bio = Bio.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    contact = Contact.objects.first()
    cv = CV.objects.last() #fetches the latest CV

    context = {
        "bio": bio,
        "projects": projects,
        "skills": skills,
        "contact": contact,
        "cv" : cv,
    }
    return render(request, "home.html", context)


def dashboard(request):
    bio = Bio.objects.first()
    projects = Project.objects.all()[:3]  # Show only 3 latest projects as preview
    skills = Skill.objects.all()[:4]      # Show only 4 skills as preview

    context = {
        "bio": bio,
        "projects": projects,
        "skills": skills,
    }
    return render(request, "dashboard.html", context)

def about(request):
    bio= Bio.objects.first()
    about_text = About.objects.first()

    context = {
        "bio": bio,
        "about_text": about_text,
    }
    return render(request, "about.html", context)

def skills(request):
    skills = Skill.objects.all()  
    context = {
        "skills": skills
    }
    return render(request, "skills.html", context)


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})

def contact(request):
    contact = Contact.objects.first()
    return render(request, "contact.html", {"contact": contact})
