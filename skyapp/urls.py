from django.urls import path
from skyapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from django.urls import path,include
app_name = 'skyapp'
routers = DefaultRouter()

routers.register('team_member', views.TeamMemmberView)



urlpatterns = [

    path('all_employees/', views.Testmodule.as_view({'get': 'all_Employees'}), name='all_profiles'),
    path('lastname/<str:lastname>', views.Testmodule.as_view({'get': 'search_lastname'}), name='lastname'),
    path('department_id/<int:dep_id>', views.Testmodule.as_view({'get': 'search_by_department'}), name='search_by_department'),
    path('api/', include(routers.urls))
   
    
]