from django.db import models

from stories.models import Story

class Employee(models.Model):
    
    EMP_TYPES = (
        ('D','Developer'),
        ('P','Project Manager'),
        ('T','Top Level Manager'),
    )

    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)

    emp_type = models.CharField(max_length=1,choices=EMP_TYPES, \
                                            default=0,null=False)

    stories_assigned = models.ManyToManyField(Story, blank=True)

    def __str__(self):
        return '{} {} - {}'.format(self.first_name, \
                                    self.last_name, self.emp_type)

    


class Skill(models.Model):

    skill_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class SkillLevel(models.Model):

    employee = models.ForeignKey(Employee,null=False,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,null=False,on_delete=models.CASCADE)

    score = models.FloatField(default=0)



