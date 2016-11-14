from django import forms
from django.contrib.auth.models import User
from .models import Owner, Recharge, Debit, Balance, Transfer,CodeReceived
from django.core.validators import RegexValidator


class UserReg(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[RegexValidator(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,20}', message="Password should contain Minimum 8 characters, at least 1 Uppercase Alphabet, 1 Lowercase Alphabet, 1 Number and 1 Special Character")])
    username = forms.CharField(min_length=5)
    email = forms.EmailField(required=True)

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email is already registered with us")
        return data

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class OwnerInfo(forms.ModelForm):

    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'phone_number']


class RechargeForm(forms.ModelForm):

    class Meta:
        model = Recharge
        fields = ['phone_number', 'type', 'operator', 'circle', 'plan']


class AddDebit(forms.ModelForm):

    class Meta:
        model = Debit
        fields = ['debitNumber', 'expiration', 'cvv']


class AddBalance(forms.ModelForm):

    class Meta:
        model = Balance
        fields = ['amount']


class TransferBalance(forms.ModelForm):

    class Meta:
        model = Transfer
        fields = ['phone_number', 'transfer_amount']


class CodeVerification(forms.ModelForm):

    class Meta:
        model = CodeReceived
        fields = ['verification_code']
