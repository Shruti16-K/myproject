from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="Take Servey"),
    path('signup', views.signup, name="signup",), #signup page
    path('products/<user>', views.greet, name=""),
]
