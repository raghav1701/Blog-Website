from django.db import models
from django.contrib.auth import get_user_model
from django import forms

# Create your models here.

User = get_user_model()

class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_picture = models.ImageField()

	def __str__(self):
		return self.user.username



class category(models.Model):
	title = models.CharField(max_length=20)


	def __str__(self):
		return self.title



class post(models.Model):
	title = models.CharField(max_length = 100)
	overview = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)
	comment_count = models.IntegerField(default =0)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail = models.ImageField()
	categories = models.ManyToManyField(category)
	featured = models.BooleanField()

	def __str__(self):
		return self.title

class testing(forms.Form):
	email = forms.EmailField(label ='', widget = forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'It Works... Admin will receive all the mail ID\'s in the DATABASE',
				}

			))

	def clean_email(self, *args, **kwargs):

		email = self.cleaned_data.get("email")
		if not email.endswith("@gmail.com"):
			raise forms.ValidationError("This is not a valid email")
		return email
