from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegisterUserForm, LoginForm
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event
from .utils import MyCalendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = MyCalendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        print(html_cal)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

class Home(View):
    def get(self, request):
        return render(request, 'base.html')


class RegisterUserView(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'register-user.html', {'form': form})

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['login'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password_1'],
            )
            return redirect('/')
        else:
            return HttpResponse("Wprowadzono błędne dane")

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse("Błędny login lub hasło")
        else:
            return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        form = LoginForm()
        logout(request)
        return render(request, 'base.html', {'form': form})

class ReservationView(View):
    def get(self, request):
        return render(request, 'reservation.html')