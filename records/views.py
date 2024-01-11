import decimal
from datetime import timedelta

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from records.forms import *
from records.models import *
from .serializers import ClientSerializer, EventsSerializers


@login_required(login_url='users/login/')
def index(request):
    user = request.user
    therapist_records_next = None
    client_records_next = None
    if user.user_type == 'TH':
        therapist = Therapist.objects.get(user=request.user)
        therapist_records_next = therapist.get_records
    elif user.user_type == 'CL':
        client = Clients.objects.get(user=request.user)
        # client_records_next = client.get_next_records
        client_records = Records.objects.filter(
            (Q(client__user=user) | Q(date__lt=timezone.now())) &
            ~Q(status='Отменено')
        )

    search_query = request.GET.get('search', '')
    selected_method_id = request.GET.get('method', '')

    methods = Methods.objects.all()

    if search_query or selected_method_id:
        query = Q()
        if search_query:
            query |= Q(first_name__startswith=search_query) | Q(last_name__icontains=search_query)
        if selected_method_id:
            query &= ~Q(methods__id=selected_method_id)
        therapists = Therapist.objects.filter(query)
    else:
        therapists = Therapist.objects.all()

    context = {
        'tittle': 'Домашний экран',
        'client_records': client_records,
        'therapist_records': therapist_records_next,
        'therapists': therapists,
        'methods': methods,
    }
    return render(request, 'records/index.html', context)


@login_required(login_url='users/login/')
def lastrecords(request):
    user = request.user
    therapist_records_past = None
    client_records_past = None
    if user.user_type == 'TH':
        therapist = Therapist.objects.get(user=request.user)
        therapist_records_past = therapist.get_past_records()
    elif user.user_type == 'CL':
        client = Clients.objects.get(user=request.user)
        client_records_past = client.get_past_records
    context = {
        'tittle': "История консультаций",
        'client_records': client_records_past,
        'therapist_records': therapist_records_past,
        'user': user,
        'therapists': Therapist.objects.all(),
    }
    return render(request, 'records/lastrecords.html', context)


@login_required(login_url='users/login/')
def cancel_record(request, record_id):
    user = request.user
    record = Records.objects.get(id=record_id)
    if user.user_type == 'CL':
        record.client = None
        record.save()
    elif user.user_type == 'TH':
        record.delete()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='users/login/')
def addrecord(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.therapist = Therapist.objects.get(user=request.user)
            record.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = AddRecordForm()
    context = {
        'form': form,
        'tittle': 'Добавить запись'
    }
    return render(request, 'records/addrecord.html', context)


@login_required(login_url='users/login/')
def therapists(request):
    therapists = Therapist.objects.all()
    selected_methods = request.GET.getlist('methods')
    selected_feelings = request.GET.getlist('feelings')
    selected_events = request.GET.getlist('events')
    selected_price = request.GET.getlist('price')
    selected_date = request.GET.getlist('date')
    if request.method == 'GET':
        if selected_events:
            therapists = therapists.filter(events__name__in=selected_events).distinct()
        if selected_feelings:
            therapists = therapists.filter(feelings__name__in=selected_feelings).distinct()
        if selected_methods:
            therapists = therapists.filter(methods__name__in=selected_methods).distinct()

    selected_next_record_date = request.GET.get('next_record_date')
    selected_next_record_price = request.GET.get('next_record_price')

    if selected_next_record_date:
        therapists = therapists.filter(
            records_set__date__gte=datetime.strptime(selected_next_record_date, "%Y-%m-%d"),
            records_set__date__lte=datetime.strptime(selected_next_record_date, "%Y-%m-%d") + timedelta(days=1)
        ).distinct()

    if selected_next_record_price:
        price_range = selected_next_record_price.split('-')
        if len(price_range) == 2:
            min_price, max_price = map(decimal.Decimal, price_range)
            therapists = therapists.annotate(
                next_price=F('records_set__price')
            ).filter(
                next_price__gte=min_price,
                next_price__lte=max_price
            ).distinct()

    paginator = Paginator(therapists, 10)
    page = request.GET.get('page')
    therapists = paginator.get_page(page)

    context = {
        'tittle': 'Терапветы',
        'therapists': therapists,
        # 'records': Records.objects.all(),
        'methods': Methods.objects.all(),
        'feelings': Feelings.objects.all(),
        'events': Events.objects.all(),
        'selected_methods': selected_methods,
        'selected_feelings': selected_feelings,
        'selected_events': selected_events,
        'selected_price': selected_price,
        'selected_date': selected_date,
        'selected_next_record_date': selected_next_record_date,
        'selected_next_price': selected_next_record_price
    }

    return render(request, 'records/therapists.html', context)


@login_required(login_url='users/login/')
def therapist_profile(request, therapist_id):
    therapist = get_object_or_404(Therapist, pk=therapist_id)
    records = therapist.get_records()
    context = {
        'records': records,
        'therapist': therapist
    }
    return render(request, 'records/therapist_profile.html', context)


@login_required(login_url='users/login/')
def record_update(request):
    if request.method == 'POST':
        client = Clients.objects.get(user=request.user)
        record_id = request.POST.get('record_id')
        record = Records.objects.get(id=record_id)
        record.client = client
        record.save()
        HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse(index))


@login_required(login_url='users/login/')
def future_appointments_view(request, therapist_id):
    therapist = Therapist.objects.get(id=therapist_id)

    future_appointments = Records.objects.filter(
        Q(therapist=therapist) &
        Q(date__gt=timezone.now()) &
        ~Q(status='Отменено')
    ).distinct()

    context = {
        'future_appointments': future_appointments,
    }

    return render(request, 'records/future_appointments.html', context)


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    @action(methods=['GET'], detail=False)
    def count(self, request):
        clients_count = Clients.objects.count()
        return Response({"clients_count": clients_count})


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers

    @action(methods=['POST'], detail=True)
    def rate_event(self, request, pk=None):
        event = self.get_object()
        try:
            new_rating = float(request.data.get('rating'))
            if new_rating < 1 or new_rating > 5:
                return Response({"message": "Rating must be between 1 and 5"}, status=status.HTTP_400_BAD_REQUEST)

            event.update_rating(new_rating)
            return Response({"message": "Event rated successfully", "average_rating": event.average_rating},
                            status=status.HTTP_200_OK)

        except (TypeError, ValueError):
            return Response({"message": "Invalid rating"}, status=status.HTTP_400_BAD_REQUEST)
