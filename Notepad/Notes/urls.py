from django.urls import path
from Notes import views
urlpatterns=[
    path('abc',views.func1,name="a1")
]