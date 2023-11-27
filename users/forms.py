from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator
from users.models import User
from records.models import Clients, Therapist, Methods, Feelings, Events


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [('CL', 'Я клиент'), ('TH', 'Я терапевт')]
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField
    first_name = forms.CharField(widget=forms.TextInput(), validators=[
        RegexValidator(
            regex='^[а-яА-ЯёЁ]+$',  # Регулярное выражение для проверки на кириллицу
            message='Введите имя на кириллице.',
            code='invalid_name'
        )
    ])
    last_name = forms.CharField(widget=forms.TextInput(), validators=[
        RegexValidator(
            regex='^[а-яА-ЯёЁ]+$',  # Регулярное выражение для проверки на кириллицу
            message='Введите имя на кириллице.',
            code='invalid_name'
        )
    ])
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form__radio'}),
                                  initial='CL')

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        user.save()

        if user_type == 'CL':
            Clients.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)
        elif user_type == 'TH':
            Therapist.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'username', 'last_name', 'first_name', 'password1', 'password2', 'user_type')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    photo = forms.ImageField(widget=forms.FileInput(), required=False)
    email = forms.EmailField()
    description = forms.Textarea()
    methods = forms.ModelMultipleChoiceField(queryset=Methods.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkboxes__input'}),
                                             required=False)
    feelings = forms.ModelMultipleChoiceField(queryset=Feelings.objects.all(),
                                              widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkboxes__input'}),
                                              required=False)
    events = forms.ModelMultipleChoiceField(queryset=Events.objects.all(),
                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkboxes__input'}),
                                            required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = user.user_type
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        methods = self.cleaned_data.get('methods')
        feelings = self.cleaned_data.get('feelings')
        events = self.cleaned_data.get('events')
        description = self.cleaned_data.get('description')
        photo = self.cleaned_data.get('photo')
        if user_type == 'CL':
            client = Clients.objects.get(user=user)
            client.first_name = first_name
            client.last_name = last_name
            client.email = email
            if photo:
                client.photo = photo
            client.save()
        elif user_type == 'TH':
            therapist = Therapist.objects.get(user=user)
            therapist.first_name = first_name
            therapist.last_name = last_name
            therapist.email = email
            therapist.methods.set(methods)
            therapist.feelings.set(feelings)
            therapist.events.set(events)
            therapist.description = description
            if photo:
                therapist.photo = photo
            therapist.save()
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'photo', 'email', 'methods', 'feelings', 'events', 'description')
