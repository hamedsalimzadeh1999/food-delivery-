from django.urls import path , include
from .views import adminloginview,adminpage,adminauth,logoutadmin,add_pizza,viewpizaa
urlpatterns = [
    path('',adminloginview ,name="adminlogin"),
    path('adminauth/',adminauth ,name="adminauth"),
    path('adminpage/',adminpage ,name="adminpage"),
    path('logout/',logoutadmin ,name="logout"),
    path('addpizza/',add_pizza,name="addpizza"),
    path('view/',viewpizaa,name="pizzaview"),
    
]
