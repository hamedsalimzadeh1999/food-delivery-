from django.urls import path , include
from .views import adminloginview,adminpage,adminauth,logoutadmin
urlpatterns = [
    path('',adminloginview ,name="adminlogin"),
    path('adminauth/',adminauth ,name="adminauth"),
    path('adminpage/',adminpage ,name="adminpage"),
    path('logout/',logoutadmin ,name="logout"),
    
]
