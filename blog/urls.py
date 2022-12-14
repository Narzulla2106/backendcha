from django.contrib import admin
from django.urls import path
from backend.views import HomeView,AboutView
urlpatterns = [
path('admin/', admin.site.urls),
path('', HomeView.as_view()),
path('about/', AboutView.as_view(), name='about' )
]

