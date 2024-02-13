from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):

    '''
    Customer Sign Up Form - OTP Implemented
    '''

    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1900, 2025)))
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'date_of_birth',
                  'gender', 'phone_number', 'password', 're_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError(
                "Password don't match - Please try again"
            )