from django.shortcuts import render,redirect
import json
from django.views import View
from django.http import HttpResponse,JsonResponse
def homepage(request):
    return render(request,'index.html')


#handling json files
class json_handle(View):
    def get(self, request):
        with open('data.json', 'r') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)