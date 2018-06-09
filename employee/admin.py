from django.contrib import admin

from .models import Employee, Skill, SkillLevel

# Register your models here.

admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(SkillLevel)

