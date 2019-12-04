from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(
			widget=forms.TextInput(
				attrs={
					"class":"form-control",
					"id":"form_full_name",
					"placeholder":"Your Full Name"
					}
				)
			)
	email = forms.EmailField(widget=forms.EmailInput(
				attrs={
					"class":"form-control",
					"id":"form_full_name",
					"placeholder":"Your Email"
					}
				)
			)
	content = forms.CharField(widget=forms.Textarea(
				attrs={
					"class":"form-control",
					"id":"form_content",
					"placeholder":"Your Message"
					}
				)
			)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not '@gmail.com' in email:
			raise forms.ValidationError("Email has to be gmail.com")

class LoginForm(forms.Form):
	username = forms.CharField(
			widget=forms.TextInput(
				attrs={
					"class":"form-control",
					"id":"form_usenrname",
					"placeholder":"User Name"
					}
				)
			)
	password = forms.CharField(
			widget=forms.PasswordInput(
				attrs={
					"class":"form-control",
					"id":"form_password",
					"placeholder":"Password"
					}
				)
			)

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
				attrs={
					"class":"form-control",
					"id":"form_usenrname",
					"placeholder":"User Name"
					}
				))
	email = forms.EmailField(widget=forms.TextInput(
				attrs={
					"class":"form-control",
					"id":"form_usenrname",
					"placeholder":"Email"
					}
				))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}), label='Confirm Password')
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("User Name is taken. Please select another username")
		return username
	def clean(self):
		data = self.cleaned_data
		password= self.cleaned_data.get('password')
		password2= self.cleaned_data.get('password2')
		if password2 != password:
			raise forms.ValidationError("Passwords must match")
		return data
