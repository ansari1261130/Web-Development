from django.urls import path
from shop import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.details,name='details'),
    path('checkout/',views.checkout,name='checkout'),

]