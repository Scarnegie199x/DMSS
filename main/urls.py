from django.urls import path

from .views import HomePageView, error_page

urlpatterns = [
    path('', HomePageView.as_view(), name = "home")
]

handler404 = 'main.views.error_page'