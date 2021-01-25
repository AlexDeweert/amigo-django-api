from django.http import HttpResponse
from amigoapi.models import User

def get_user(response):
    user = User.objects.create(
        email = "testemail@gmail.com",
        password = "12345",
        api_token = "i0j12d1209dj01j2"
    )
    return HttpResponse("Created a user {}".format(user))
