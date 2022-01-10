from django.http import HttpResponse

from django.shortcuts import render

from .models import User, Company

def index(request):
    return HttpResponse("You're off to a good start, but there's nothing to see here. We're only using the API.")

def users(request):

    manager_list = []
    herd_cats = []

    #if the user was logged into a session get their .company attribute
    logged_in_user = request.user

    #I'll just use last entry
    company_id = Company.objects.last().id


    user_names = User.objects.filter(company = company_id)



    has_boss = User.objects.exclude(reports_to__isnull=True)

    for dude in has_boss:
        if dude.reports_to not in manager_list:
            manager_list.append(dude.reports_to)

    _do_not_have_manager = User.objects.exclude(reports_to__isnull=False)

    for dude in _do_not_have_manager:
        if dude.first_name not in herd_cats:
            herd_cats.append(dude.first_name)

    return render(request, "users.html", {'user_names': user_names, 'logged_in':logged_in_user,'company':company_id,'manager_list':manager_list,'herd_cats':herd_cats})
