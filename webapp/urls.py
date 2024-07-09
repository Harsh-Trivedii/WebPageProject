from django.urls import path
from webapp import views

urlpatterns=[
    path('',views.homepage_view,name='home'),
    path('date',views.currentdatetime_view,name='date'),
    path('userdata',views.userdata_view,name='userdata'),
    path('saveduserdata/', views.saveduserdata_view, name='saveduserdata'),
]