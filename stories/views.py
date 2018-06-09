from django.shortcuts import render
from django.http import JsonResponse
from .utils import calc_correlation
from django.views.decorators.csrf import csrf_exempt


import json 


def get_pm_stories(request,pm_id):
    pass

@csrf_exempt
def corelation(request):
    if request.method == 'POST':
        try:
            keyword = json.loads(request.body)['keyword']
            print(keyword)
            return JsonResponse({'words': calc_correlation(keyword)})
        except:
            return JsonResponse({},status=400)

    return JsonResponse({},status=400)

