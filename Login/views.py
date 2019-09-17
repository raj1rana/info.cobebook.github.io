from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm


# Home page
def home(request):
	return render(request, 'Login/index.html')


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/admin')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = LoginForm()
	return render(request, 'Login/login.html', {'form': form})
