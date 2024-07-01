import os

from django.db import models
import datetime


# Create your models here.

def get_file_name(instance, filename):
    old_name = filename
    time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    file_name = "%s%s" % (time_now, old_name)
    return os.path.join('uploads/', file_name)


class Header(models.Model):
    id = models.AutoField(primary_key=True)
    header_name = models.CharField(max_length=50, null=False, blank=False)
    header_subtitle = models.CharField(max_length=50, null=False, blank=False)
    header_attr = models.CharField(max_length=50, null=False, blank=False)
    header_image = models.ImageField(upload_to=get_file_name, null=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.header_name


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, blank=False)
    institution = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    field_of_study = models.CharField(max_length=50, null=False, blank=False)
    marks = models.CharField(max_length=50, null=False, blank=False)
    duration = models.CharField(max_length=50, null=False, blank=False)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title


class SoftSkill(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=50, null=False, blank=False)
    skill_percentage = models.CharField(max_length=50, null=False, blank=False)
    skill_hex_color = models.CharField(max_length=7, null=False, blank=False)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.skill_name


class HardSkill(models.Model):
    id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=50, null=False, blank=False)
    skill_percentage = models.CharField(max_length=50, null=False, blank=False)
    skill_hex_color = models.CharField(max_length=7, null=False, blank=False)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.skill_name


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    designation = models.CharField(max_length=50, null=False, blank=False)
    duration = models.CharField(max_length=50, null=False, blank=False)
    sector = models.CharField(max_length=50, null=False, blank=False)
    website = models.CharField(max_length=100, null=False, blank=False)
    company_logo = models.ImageField(upload_to=get_file_name, null=True)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.company_name


class ExperienceImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to=get_file_name, null=False, blank=False)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, null=False, blank=False)
    project_description = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False)
    project_link = models.CharField(max_length=50, null=False, blank=False)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.project_name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=255, null=False, blank=False)
    header = models.ForeignKey(Header, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name
