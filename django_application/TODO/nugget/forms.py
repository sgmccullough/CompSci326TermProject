from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Nugget, NuggetAttribute, Inventory, BattleInstance, Profile, Friend

mouth = (
    ('h', 'hyper'),
    ('n', 'nervous'),
    ('hu', 'hungry'),
    ('c', 'content'),
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
    mouth_status = forms.ChoiceField(widget=forms.Select(attrs={'id': 'evt_mouth'}), choices=mouth, label='Mouth')

    class Meta:
        model = NuggetAttribute
        fields = ('color', 'nug_size', 'eye_size', 'mouth_size', 'nugget_status', 'eye_status', 'mouth_status', )

class InventoryForm(ModelForm):
    OPTIONS = (
                ("feed", "Feed"),
                ("discard", "Discard"),
                ("sell", "Sell"),
              )
    ItemOptions = forms.ChoiceField(widget=forms.Select(attrs={'onChange': 'form.submit()'}), choices=OPTIONS, label='Select an Action')
    ItemName = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Inventory
        fields = ('ItemOptions', 'ItemName')

class NewBattle(forms.ModelForm):

    #usr_id = Profile.objects.get(usr=request.user)
    fr_choices = (
        ('0', '-'),
    )
    # usr_id = forms.ModelChoiceField(
    # friends = Friend.objects.get(current_user=usr_id)
    # friends_names = getattr(friends, 'users')
    opponents = forms.ChoiceField(widget=forms.Select)
    #opponents = forms.ModelChoiceField(widget=forms.Select, queryset=Friend.objects.filter(current_user=self.user).values('users'))

    def __init__(self, user, *args, **kwargs):
        #self.user = user
        super(NewBattle, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)

        thisUser = Profile.objects.get(usr=user)

        if user:
            friends = Friend.objects.get(current_user=thisUser)#.values('users')
            friendChoices = getattr(friends, 'users')
            choices = []
            for i in friendChoices.iterator():
                choices.append((str(i.usr.username), str(i.usr.username)))
            self.fields['opponents'].choices = choices

        # self.fields['opponents'].queryset = Friend.objects.filter(current_user=self.user).values('users')
        # super(NewBattle, self).__init__(*args, **kwargs)
        # self.fields['opponents'].queryset = User.objects.filter(pk=user.id)
    #forms.ChoiceField(widget=forms.Select, choices=???, label='Opponent Options')

    class Meta:
        model = BattleInstance
        fields = ('opponents',)
