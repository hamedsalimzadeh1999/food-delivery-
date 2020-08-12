from django.urls import path , include
from .views import adminloginview,adminpage,adminauth,logoutadmin,add_pizza,viewpizaa,editpizaa,deletepizaa,HomePage,signupuser,logoutuser,userauth,loginuser,customerpage
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
    path('editpizaa/<int:pizzaid>/',editpizaa,name="editpizaa"),
    path('view/deletpizaaid/<int:pizzaid>/',deletepizaa , name='delet'),
    path('customerpage/',customerpage,name='customerpage')
]
