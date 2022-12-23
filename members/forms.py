from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, min_length=4)
    password = forms.CharField(max_length=50, min_length=8)
    password2 = forms.CharField(max_length=50, min_length=8)

    class Meta:
        model = User
        fields = ("username", "password", 'password2')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password.isalpha() and password2 == password:
            return password
        raise ValidationError("Параль должен содержать только буквы!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
