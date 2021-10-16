from django.urls import path, re_path
from account.views import (
    RegisterView,
    CustomLoginView,
    logout,

)

app_name = 'account'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
 

]