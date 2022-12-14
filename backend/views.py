from django.shortcuts import render
from django.views.generic import *


class AboutView(TemplateView):
  template_name = 'about.html'
class HomeView(TemplateView):
  template_name = 'index.html'


