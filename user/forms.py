from django import forms

class SignupForm(forms.Form):

    company_name = forms.CharField(
        max_length=100
    )

    name = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    phone = forms.CharField(
        max_length=15
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )


class LoginForm(forms.Form):
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )