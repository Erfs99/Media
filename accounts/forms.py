from django import forms
from .models import User
from .models import Profile
from django.core import validators
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


class SignupForm(forms.ModelForm):
    phone=forms.IntegerField(required=True,widget=forms.NumberInput(  attrs={         
                "class": "form-control"
            }))
    class Meta:
        model = User
        fields = ['phone', ]


class ProfileView(forms.ModelForm):
    user_name=forms.CharField(validators=[validators.MinLengthValidator(3)])
    first_name=forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            "placeholder":"optional",
            "class": "form-control"}))

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional",
            "class": "form-control"}))

    YEARS = [x for x in range(1940, 2003)]
    birthdate = forms.DateField(initial="1994-06-21", widget=forms.SelectDateWidget(years=YEARS,))

    class Meta:
        model = Profile
        fields = ["user_name","first_name", "last_name", "gender", "birthdate"]
    def clean(self):
        user_name=self.cleaned_data["user_name"]  
        if Profile.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("This username is already taken")
       


class ProfileView2(forms.ModelForm):
    bio = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    class Meta:
        model = Profile
        fields = ["profile_image", "bio"]


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))

    bio = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            "placeholder": "optional"}))
    YEARS = [x for x in range(1940, 2003)]
    birthdate = forms.DateField(initial="1994-06-21", widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender',
                  'profile_image', 'bio', 'account_type', 'birthdate']
