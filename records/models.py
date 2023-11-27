from datetime import datetime

from django.db import models
from django.db.models import Min
from simple_history.models import HistoricalRecords

from users.models import User


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client', null=True)
    photo = models.ImageField(upload_to='user_images', blank=True, null=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128)
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name

    @property
    def get_next_records(self):
        return self.records_set.filter(date__gte=datetime.now()).order_by('date', 'time')

    def get_past_records(self):
        return self.records_set.filter(date__lt=datetime.now()).order_by('-date', '-time')


class Methods(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Feelings(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='therapist', null=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128)
    methods = models.ManyToManyField(Methods)
    feelings = models.ManyToManyField(Feelings)
    events = models.ManyToManyField(Events)
    photo = models.ImageField(upload_to='user_images', blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username

    @property
    def next_record(self):
        return self.records_set.filter(date__gte=datetime.now()).aggregate(Min('date'))['date__min']

    @property
    def next_record_price(self):
        next_record = self.records_set.filter(date__gte=datetime.now()).order_by('date', 'time').first()
        if next_record:
            return next_record.price
        return None

    def get_records(self):
        return self.records_set.filter(date__gte=datetime.now()).order_by('date', 'time')

    def get_past_records(self):
        return self.records_set.filter(date__lt=datetime.now()).order_by('-date', '-time')


class Records(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    # therapist_photo = models.ForeignKey(, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Clients, null=True, blank=True, on_delete=models.SET_NULL)
    history = HistoricalRecords()

    @property
    def therapist_photo(self):
        if self.therapist.photo:
            return self.therapist.photo

    def __str__(self):
        return f'{self.therapist.first_name} record'
