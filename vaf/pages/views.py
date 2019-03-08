from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, lot_size_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor
from pages.models import Photoi, Photoa

from django.contrib.auth.decorators import login_required


def index(request):
    return HttpRequest{'<h1> Hello World </h1>'}
