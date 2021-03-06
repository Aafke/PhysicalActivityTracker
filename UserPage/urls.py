from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_activity_record

urlpatterns = [
    url(r'home$', home, name="UserPage_home"),
    url(r'login$',
        LoginView.as_view(template_name="UserPage/login_form.html"),
        name="UserPage_login"),
    url(r'logout$',
        LogoutView.as_view(),
        name="UserPage_logout"),
    url(r'new_activity_record',
        new_activity_record,
        name="UserPage_new_activity_record")
]