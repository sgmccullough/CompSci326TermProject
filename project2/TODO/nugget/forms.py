from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Nugget, NuggetAttribute

mouth = (
    ('h', 'Happy'),
    ('n', 'Nervous'),
    ('d', 'displeased'),
    ('hu', 'Hungry'),
)

eye = (
    ('w', 'Wide'),
    ('s', 'Small'),
    ('sl', 'Sleepy'),
    ('m', 'Mad'),
)

shape = (
    ('e', 'Egg-like'),
    ('r', 'Round'),
    ('t', 'Triangle'),
    ('s', 'Square'),
)

col = (
    ('honeydew', 'Honeydew'),
    ('goldenrod', 'Goldenrod'),
    ('darkgoldenrod', 'Dark Goldenrod'),
    ('sienna', 'Sienna'),
    ('burlywood', 'Burlywood'),
    ('tan', 'Tan'),
)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    birthday = forms.DateField(widget=forms.TextInput())
    # attrs={'class':'datepicker'}

    class Meta:
        model = User
        fields = ('username',  'email', 'first_name', 'last_name', 'password1', 'password2', 'birthday', )

class CreateNugget(ModelForm):
    name = forms.CharField(max_length=25)

    class Meta:
        model = Nugget
        fields = ('name', )

class CreateAttributes(ModelForm):
    color = forms.ChoiceField(widget=forms.Select(attrs={'id': 'evt_color'}), choices=col)
    nug_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'id': 'test5', 'min': 1, 'max': 100, 'id': 'evt_size'}), label='Size')
    eye_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'id': 'test5', 'min': 1, 'max': 100}), label='Eye Size')
    mouth_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'id': 'test5', 'min': 1, 'max': 100}), label='Mouth Size')
    nugget_status = forms.ChoiceField(widget=forms.Select, choices=shape, label='Shape')
    eye_status = forms.ChoiceField(widget=forms.Select, choices=eye, label='Eyes')
    mouth_status = forms.ChoiceField(widget=forms.Select, choices=mouth, label='Mouth')

    class Meta:
        model = NuggetAttribute
        fields = ('color', 'nug_size', 'eye_size', 'mouth_size', 'nugget_status', 'eye_status', 'mouth_status', )
