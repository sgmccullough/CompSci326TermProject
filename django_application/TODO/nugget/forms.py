from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Nugget, NuggetAttribute, Inventory, BattleInstance, Profile, Friend, InventoryItems, Battle, Chat, ChatMessage, Forum, ForumComments

mouth = (
    ('hyper', 'Happy'),
    ('nervous', 'Nervous'),
    ('hungry', 'Hungry'),
    ('content', 'Content'),
)

eye = (
    ('w', 'Wide'),
    ('s', 'Small'),
    ('sl', 'Sleepy'),
    ('m', 'Mad'),
)

shape = (
    ('e', 'Egg'),
    ('c', 'Circle'),
)

col = (
    ('honeydew', 'Honeydew'),
    ('goldenrod', 'Goldenrod'),
    ('darkgoldenrod', 'Dark Goldenrod'),
    ('sienna', 'Sienna'),
    ('burlywood', 'Burlywood'),
    ('tan', 'Tan'),
    ('coral', 'Coral'),
    ('darkcyan', 'Cyan'),
    ('deepskyblue', 'Sky Blue'),
)

invOpts = (
    ("feed", "Feed"),
    ("discard", "Discard"),
    ("sell", "Sell"),
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
    #nug_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'id': 'size', 'min': 50, 'max': 100, 'id': 'evt_size', 'hidden': 'hidden'}), label='Size')
    eye_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'id': 'eyesize', 'min': 15, 'max': 30}), label='Eye Size')
    #mouth_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'id': 'mouthsize', 'min': 1, 'max': 100, 'hidden': 'hidden'}), label='Mouth Size')
    nugget_status = forms.ChoiceField(widget=forms.Select(attrs={'id': 'shape'}), choices=shape, label='Shape')
    #eye_status = forms.ChoiceField(widget=forms.Select(attrs={'hidden': 'hidden'}), choices=eye, label='Eyes')
    mouth_status = forms.ChoiceField(widget=forms.Select(attrs={'id': 'evt_mouth'}), choices=mouth, label='Mouth')

    class Meta:
        model = NuggetAttribute
        fields = ('color', 'eye_size', 'nugget_status', 'mouth_status', )

class InventoryForm(ModelForm):
    ItemQuantity = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number', 'min': 1, 'max': 100, 'value': 1}), label='Quantity to work with (should be less than the amount you have)')
    ItemOptions = forms.ChoiceField(widget=forms.Select, choices=invOpts, label='What do you want to do?')

    class Meta:
        model = Inventory
        fields = ('ItemQuantity', 'ItemOptions')

class InventoryFormShop(ModelForm):
    ItemQuantity = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number', 'min': 1, 'max': 100, 'value': 1}), label='Quantity to work with (should be less than the amount you have)')

    class Meta:
        model = Inventory
        fields = ('ItemQuantity',)

class ShopPurchase(ModelForm):
    ItemQuantity = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number', 'min': 1, 'max': 100, 'value': 1}), label='Quantity to work with (should be less than the amount you have)')

    class Meta:
        model = Inventory
        fields = ('ItemQuantity',)

class NewBattle(forms.ModelForm):

    #usr_id = Profile.objects.get(usr=request.user)
    fr_choices = (
        ('0', '-'),
    )

    opp_a = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=None)
    net_coins = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'hidden', 'value': '25', }))
    nug_xp = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'hidden', 'value': '5', }))
    opp_b = forms.ModelChoiceField(queryset=None, label='Choose your opponent...')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewBattle, self).__init__(*args, **kwargs)

        thisUser = Profile.objects.get(usr=self.user)

        if thisUser:
            friends = Friend.objects.get(current_user=thisUser)
            friendChoices = getattr(friends, 'users')
            self.fields['opp_b'].queryset = friendChoices
            self.fields['opp_a'].queryset = Profile.objects.filter(usr=self.user)

    class Meta:
        model = BattleInstance
        fields = ('opp_a', 'net_coins', 'nug_xp', 'opp_b' )

class BattleReset(forms.ModelForm):

    current = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'hidden', }))

    class Meta:
        model = Battle
        fields = ('current', )

class BattleResponse(forms.ModelForm):
    choices = (
        ('2', 'Accept - destroy them!'),
        ('0', 'Decline - maybe next time...'),
    )
    current = forms.ChoiceField(widget=forms.Select, choices=choices)

    class Meta:
        model = Battle
        fields = ('current', )

class ChatStart(forms.ModelForm):
    content = forms.CharField(label='Content of Post (1000 Characters)')

    class Meta:
        model = Chat
        fields = ('content',)

class IndividualMessage(forms.ModelForm):
    content = forms.CharField(label='Content of Post (1000 Characters)')

    class Meta:
        model = ChatMessage
        fields = ('content', )

class ForumPost(forms.ModelForm):
    choices = (
        ('general', 'General'),
        ('requests', 'Friend Requests'),
        ('battles', 'Battles'),
    )
    topic = forms.ChoiceField(widget=forms.Select, choices=choices)
    subject = forms.CharField(label='Subject of Post (100 Characters)')
    content = forms.CharField(label='Content of Post (1000 Characters)')
    # private = forms.BooleanField(required=True)
    #
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(NewBattle, self).__init__(*args, **kwargs)
    #
    #     thisUser = Profile.objects.get(usr=self.user)
    #
    #     if thisUser:
    #         friends = Friend.objects.get(current_user=thisUser)
    #         friendChoices = getattr(friends, 'users')
    #         self.fields['opp_a'].queryset = Profile.objects.filter(usr=self.user)

    class Meta:
        model = Forum
        fields = ('subject', 'content',)

class ForumCommentPost(forms.ModelForm):
    content = forms.CharField(label='Content of Post (1000 Characters)')

    class Meta:
        model = ForumComments
        fields = ('content', )
