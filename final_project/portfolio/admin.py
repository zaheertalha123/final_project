from django.contrib import admin
from .models import Header, Education, SoftSkill, HardSkill, Experience, Project, Contact, ExperienceImage

# Register your models here.
admin.site.register(Header)
admin.site.register(Education)
admin.site.register(SoftSkill)
admin.site.register(HardSkill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(ExperienceImage)