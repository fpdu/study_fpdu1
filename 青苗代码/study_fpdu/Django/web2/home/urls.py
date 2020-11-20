from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.index),
    path('req/info/',views.req_info)

]