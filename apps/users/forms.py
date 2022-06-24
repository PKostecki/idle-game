from django.contrib.auth.forms import UserCreationForm, User
from django.core.exceptions import ValidationError
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Adress')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

    def clean_username(self):
        cleaned_data = super().clean()
        username = User.objects.filter(username=cleaned_data["username"])
        if username.exists():
            raise ValidationError("The username is taken, please try another one")
        return cleaned_data["username"]

    def clean_email(self):
        cleaned_data = super().clean()
        print(cleaned_data["email"])
        email = User.objects.filter(email=cleaned_data["email"])
        if email.exists():
            raise ValidationError("The email is taken, please try another one")
        return cleaned_data["email"]
