from django.urls import path
from . import views
# from .views import contact_form_view


urlpatterns = [
    path('', views.home, name='base-home'),
    # path('contact/', contact_form_view, name='contact_form'),
]