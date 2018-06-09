import json
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Employee, SkillLevel, Skill
from stories.models import Story

def get_emp_list(request,emp_type):
    dev_list = Employee.objects.filter(emp_type=Employee.EMP_TYPES[0][emp_type]).values()

    dev_list = list(dev_list)

    for i in range(len(dev_list)):
        skill_level_list = list(SkillLevel.objects.filter(employee__id=dev_list[i]['id']).values('skill','score'))
        story_list = list(Story.objects.filter(employee__id=dev_list[i]['id']).values())
        
        dev_list[i]['skills'] = [{ 
            'tag' : Skill.objects.get(id=k['skill']).tag,
            'stories': story_list,
             **k } for k in skill_level_list]


    return JsonResponse({
        "devs": dev_list
    })


@csrf_exempt
def add_story(request,emp_id):
    if request.method == 'POST':
        try:
            story_data = json.loads(request.body)
            story = Story(
                project_name=story_data['name'],
                project_desc=story_data['desc'],
                skills_required=[Skill.objects.get(tag=s) for s in story_data['skills']],
                deadline=datetime.strptime(story_data['deadline'])
                )
            story.save()
            return JsonResponse({},status=200)
        except:
            return JsonResponse({},status=400)
    return JsonResponse({},status=400)
            

@csrf_exempt
def get_dev(request,emp_id):
    if request.method == 'POST':
        try:
            story_id = json.loads(request.body)['id']
            dev = Employee.objects.get(id=emp_id)
            dev.stories_assigned.add(Story.objects.get(id=story_id))
            return JsonResponse({},status=200)
        except:
            return JsonResponse({},status=400)
        
    dev = Employee.objects.filter(id=emp_id).values()
    if len(dev) == 0:
        return JsonResponse({})
    dev = dev[0]
    
    return JsonResponse(dev)
    