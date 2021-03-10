from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Req: The HTTP Request
def main_url(req):
	return HttpResponse("<h1>Ola k ase</h1>")
