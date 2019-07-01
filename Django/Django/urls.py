from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from Restauracja.views import Home, RegisterUserView, LoginView, LogoutView, CalendarView, ReservationView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name="home_page"),
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    path('reservation/', ReservationView.as_view(), name='reservation')
]
