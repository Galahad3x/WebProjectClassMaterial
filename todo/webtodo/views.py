from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Req: The HTTP Request
from .models import Task


def main_url(req):
	tsks = Task.objects.order_by('-urgency')

	ctx = {"tasks": tsks}
	return render(req, "webtodo/tasklist.html", ctx)

# tasks_names = [t.text for t in tsks]
# text = ",".join(tasks_names)
# return HttpResponse("<h2>Ola k ase</h2>\n<p>"+text+"</p>")
