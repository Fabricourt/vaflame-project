from django.shortcuts import render
from django.http import HttpResponse
from partners.models import Partner
from team.models import Team
from testaments.models import Testament




from django.contrib.auth.decorators import login_required


def index(request):
    partners = Partner.objects.order_by('-membership_date').filter(is_published=True)[:4]
    testaments = Testament.objects.order_by('-post_date').filter(is_published=True)[:3]
    
   
    context = {
        'partners': partners,
        'testaments': testaments,
       
       
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all Team
    team = Team.objects.order_by('-hire_date')

    # Get MVP
    mvp_team = Team.objects.all().filter(is_mvp=True)

    context = {
        'teams': team,
        'mvp_team': mvp_team
    }

    return render(request, 'pages/about.html', context)

