from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('addNGO', views.AddNGOForm.as_view(), name='add_ngo'),
    path('listview/', views.NGOList.as_view(), name='listview'),
    path('<int:pk>', views.NGODetails.as_view(), name='detail'),
]
