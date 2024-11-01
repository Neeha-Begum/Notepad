from django.urls import path
from Contacts import views
urlpatterns=[
    path('contact',views.func1,name="c1"),
    path('update',views.func2,name="u1")
]