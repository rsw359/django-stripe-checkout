# from django.shortcuts import render
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.html'

@csrf_exempt
def stripe_config(request):#handles XHR requests
  if request.method == 'GET':
    stripe_config = {'public_key': settings.STRIPE_PUBLISHABLE_KEY}
    return JsonResponse(stripe_config, safe=False)

