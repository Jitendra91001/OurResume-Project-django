from django.urls import path
from.import views

urlpatterns = [
    path('index/',views.index),
    path('xyz',views.home,name='xyz'),
    path('contact',views.signup,name='cdata'),
    path('resume',views.cv,name='rsmdata'),
    path('certificate',views.marksheet,name='crftdata'),
]