from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

def generate_username_sample():
    prefix = fake.prefix_nonbinary().replace('.', '_')
    first_name = fake.first_name_nonbinary()
    color = fake.color_name()
    random_letter = fake.random_letter()
    random_number = fake.random_number(2)

    return f"{prefix}{first_name}_{color}_{random_letter}{random_number}"

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-lg',
        'autocomplete':'username'}))
    password = forms.CharField(help_text='Required', label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Our secret handshake',
        'class': 'w-full py-4 px-6 rounded-lg',
        'autocomplete':'current-password'}))

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'accept_suggested_username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    INPUT_STYLES = 'w-full py-4 px-6 rounded-lg'


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.suggested_username = generate_username_sample()
        self.fields['username'].widget.attrs.update({
            'placeholder': f'Choose a cool username, like {self.suggested_username}',
            'class': 'w-full py-4 px-6 rounded-lg'
        })  
    username = forms.CharField(max_length=30, help_text='Required', widget=forms.TextInput(attrs={
        'class': INPUT_STYLES,
        'autocomplete':'username'}))
    accept_suggested_username = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'id': 'accept-suggested',
        'label': 'Accept suggested username: ',
        'onclick': 'acceptSuggestedName()'}))
    email = forms.EmailField(max_length=254, help_text='Required', widget=forms.EmailInput(attrs={
        'placeholder': 'Where can we spam you?',
        'class': INPUT_STYLES}))
    first_name = forms.CharField(max_length=50, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'What do your friends yell when they see you?',
        'class': INPUT_STYLES}))
    last_name = forms.CharField(max_length=50, help_text='Required', widget=forms.TextInput(attrs={
        'placeholder': 'You know, the name you hide when you\'re famous.',
        'class': INPUT_STYLES,
        'autocomplete':'family-name'}))
    password1 = forms.CharField(help_text='Required', label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Your secret handshake in text form.',
        'class': INPUT_STYLES,
        'autocomplete':'new-password'}))
    password2 = forms.CharField(help_text='Required', label='Repeat password', widget=forms.PasswordInput(attrs={
        'placeholder': 'You sure? Type that secret handshake again.',
        'class': INPUT_STYLES,
        'autocomplete':'new-password'}))
