from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# handler


def say_hello(request):
    # pull data
    # send emails or transform data
    return render(request, "index.html", {"name": "Saubhagya"})
