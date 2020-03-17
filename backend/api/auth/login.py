from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView



def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return HttpResponse({'token': token.key})
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
        pass




