from django.shortcuts import render
from django.http import JsonResponse
import json

key_list = [i for i in range(100) if i%10 == 0 and i%2 == 0]
value_list = [i for i in range(10)]
dict_list = dict(zip(key_list, value_list))
def dumps(list):
    return json.dumps(list)
def home(request):
    json = dumps(dict_list)
    return JsonResponse(json)