from django import forms
from django.contrib.auth import authenticate
from .models import User


class UserLoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.EmailInput({"class": "form-control"}), required=True)
    password = forms.CharField(
        widget=forms.PasswordInput({"class": "form-control"}), required=True)

    def clean(self):
        clean_data = super().clean()
        user = authenticate(
            self.request,
            username=clean_data["email"],
            password=clean_data['password'])

        if user is not None:
            clean_data['user'] = user
            return clean_data
        else:
            raise forms.ValidationError('credential is invalid')


class UserRegisterFrom(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(), required=True, label="کلمه عبور"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(), required=True, label="تکرار کلمه عبور"
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'mobile'
        )

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.pop("password1", None)
        password2 = cleaned_data.pop("password2", None)
        if password1 and password2 and password1 != password2:
            self.add_error(
                'password2',
                forms.ValidationError('در وارد کردن کلمه عبور دقت کنید', code='password_mismatch'))
        cleaned_data.setdefault('password', password1)
        return cleaned_data

    def save(self, commit: bool = ...):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
