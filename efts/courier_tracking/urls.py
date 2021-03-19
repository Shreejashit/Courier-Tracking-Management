from django.urls import path
from.import views
urlpatterns = [
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    path('home',views.home,name="home"),
    path('enterprice',views.enterprice,name="enterprice"),
    path('coubk',views.coubk,name="coubk"),
    path('coutk',views.coutk,name="coutk"),
    path('billing/',views.billing,name="billing"),
    path('billing_table/quick_receipt/<int:id>',views.billing_table_quick_receipt,name="billing"),
    path('ofd',views.outfordelivery,name= "ofd" ),
    path('report',views.report,name="report"),
]