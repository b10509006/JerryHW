from django.shortcuts import render_to_response
from .models import personal
# Create your views here.
def index(request):
	Personal= personal.objects.all()
	return render_to_response('sarbee/heLLO.html',locals())