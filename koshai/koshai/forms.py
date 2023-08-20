from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    phone_number = forms.CharField(max_length=32, label="Phone number", required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'password1', 'password2', 'first_name', 'last_name', 'nickname', 'role']



	# def __init__(self, *args, **kwargs):
	# 	super(SignUpForm, self).__init__(*args, **kwargs)

	# 	self.fields['username'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password1'].widget.attrs['class'] = 'form-control'
	# 	self.fields['password2'].widget.attrs['class'] = 'form-control'