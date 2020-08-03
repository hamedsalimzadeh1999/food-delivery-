from django.urls import path , include
from .views import adminloginview,adminpage,adminauth,logoutadmin,add_pizza,viewpizaa,editpizaa,deletepizaa
urlpatterns = [
    path('',adminloginview ,name="adminlogin"),
    path('adminauth/',adminauth ,name="adminauth"),
    path('adminpage/',adminpage ,name="adminpage"),
    path('logout/',logoutadmin ,name="logout"),
    path('addpizza/',add_pizza,name="addpizza"),
    path('view/',viewpizaa,name="pizzaview"),
    path('editpizaa/<int:pizzaid>/',editpizaa,name="editpizaa"),
    path('view/deletpizaaid/<int:pizzaid>/',deletepizaa , name='delet'),
    
]
