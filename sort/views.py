from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .sort import sort_me
# Create your views here.
# def sort_slots(request):
# 		f=sort_me()
# 		return HttpResponse(request,"<p>Done</p>",{})