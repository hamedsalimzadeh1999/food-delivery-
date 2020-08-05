from django.urls import path , include
from .views import adminloginview,adminpage,adminauth,logoutadmin,add_pizza,viewpizaa,editpizaa,deletepizaa,HomePage,signupuser,coustomerpage,logoutuser,userauth,loginuser
urlpatterns = [
    path('',HomePage ,name="index"),
    path('signup/',signupuser ,name="signup"),
    path('login/',adminloginview ,name="adminlogin"),
    path('customauth/',userauth , name='userauth'),
    path('adminauth/',adminauth ,name="adminauth"),
    path('adminpage/',adminpage ,name="adminpage"),
    path('logout/',logoutadmin ,name="logout"),
    path('addpizza/',add_pizza,name="addpizza"),
    path('view/',viewpizaa,name="pizzaview"),
    path('userloginpage/',loginuser,name='userlogin'),
    path('customerpage',coustomerpage , name='userpage'),
    path('editpizaa/<int:pizzaid>/',editpizaa,name="editpizaa"),
    path('view/deletpizaaid/<int:pizzaid>/',deletepizaa , name='delet'),
    
]
