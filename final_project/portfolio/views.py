from django.shortcuts import render, HttpResponse
from .models import Header, Education, SoftSkill, HardSkill, Experience, Project, Contact, ExperienceImage


# Create your views here.

def portfolio(request):
    user = 3
    header = Header.objects.get(id=user)
    education = Education.objects.filter(header=user)
    soft_skill = SoftSkill.objects.filter(header=user)
    hard_skill = HardSkill.objects.filter(header=user)
    experience = Experience.objects.get(header=user)
    projects = Project.objects.filter(header=user)
    experienceImage = ExperienceImage.objects.filter(header=user)
    d = {
        "Header": header, "Education": education, "SoftSkill": soft_skill,
        "HardSkill": hard_skill, "Experience": experience, "Projects": projects,
        "ExperienceImage": experienceImage
    }
    return render(request, 'portfolio.html', d)


def submit(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        to_person = request.POST['to_person']
        Contact.objects.create(name=name, email=email, subject=subject, message=message,
                               header=Header.objects.get(header_name=to_person))

    return render(request, 'form_submitted.html')
