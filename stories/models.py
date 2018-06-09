import datetime

from django.db import models

# from employee.models import Skill

class Story(models.Model):

    project_name = models.CharField(max_length=100,null=False)
    project_desc = models.TextField(verbose_name='Project Description')

    skills_required = models.ManyToManyField('employee.Skill')

    deadline = models.DateTimeField(null=False,default= datetime.datetime.now() \
                                    + datetime.timedelta(30))



