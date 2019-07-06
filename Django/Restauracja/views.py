from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterUserForm, LoginForm, TableReservationForm
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event, Table, Accept_reservation
from .utils import MyCalendar
from django.core.mail import send_mail
from django.conf import settings


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
        return render(request, 'home-page.html')

class About(View):
    def get(self, request):
        return render(request, 'about.html')

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
        form = TableReservationForm()
        day = request.GET.get('numer')
        return render(request, "reservation.html", {"form": form, 'day': day})

    def post(self, request):
        form = TableReservationForm(request.POST)
        reservation_date = datetime.today()
        day = datetime(reservation_date.date().year, reservation_date.date().month, int(request.POST.get('day')))
        if form.is_valid():
            table_size = form.cleaned_data['table_size']
            time_reservation = form.cleaned_data['time_reservation']
            new_reservation = Table.objects.create(table_size=table_size, time_reservation=time_reservation,
                                                   date_reservation=day)
            new_reservation.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Formularz został nie poprawnie wypełnony")


class AcceptionView(View):
    def get(self, request):
        reservation_to_accept = Table.objects.last()
        return render(request, 'acception.html', {"to_accept": reservation_to_accept})

    def post(self, request):
        if request.POST.get('btn') == "Akceptuj":
            accepted = Table.objects.last()
            accepted.reservation = Accept_reservation.objects.create(table_size=accepted.table_size,
                                                                     time_reservation=accepted.time_reservation,
                                                                     date_reservation=accepted.date_reservation)
            accepted.reservation.save()
            accepted.delete()
            email = request.user.email
            send_mail('Rezerwacja','Twoja rezerwacja została zatwierdzona', settings.EMAIL_HOST_USER, [email])
            return HttpResponseRedirect("/acception")
        else:
            accepted = Table.objects.last()
            accepted.delete()
            email = request.user.email
            send_mail('Rezerwacja','Niestety twoja rezerwacja została odrzucona', settings.EMAIL_HOST_USER, [email])

            return HttpResponseRedirect("/acception")

