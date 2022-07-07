
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import ContactForm
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			html = render_to_string('contact/emails/contactform.html', {
				'name': name,
				'email': email,
				'message': message
				})

			send_mail(
			 	'Subject: Contact Form Message | From: ' + name,
			 	'this is the message', 
			 	email,
			 	['hergoku13@gmail.com'],
			 	html_message=html
			 	)
			# return redirect('index')
			# return render(request, "contact/success.html")
			return render(request, 'contact/index.html', {'name': name})


	else:
		form = ContactForm()

	return render(request, 'contact/index.html', {'form': form})