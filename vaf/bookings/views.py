from django.shortcuts import render,  redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Booking


from django.contrib.auth.decorators import login_required



@login_required
def booking(request):
  if request.method == 'POST':
    partner = request.POST['partner']
    partner_id = request.POST['partner_id']
    ministry_name = request.POST['ministry_name']
    ministry_location = request.POST['ministry_location']
    county = request.POST['county']
    address = request.POST['address']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    description = request.POST['description']
    booking_date = request.POST['booking_date']
    return_date = request.POST['return_date']
    user_id = request.POST['user_id']
    team_email = request.POST['team_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Booking.objects.all().filter(partner_id=partner_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an booking for this truck')
        return redirect('/partners/'+partner_id)

    booking = Booking(
      partner=partner, 
      partner_id=partner_id,
      ministry_name=ministry_name,
      ministry_location=ministry_location,
      county=county,
      name=name, 
      email=email, 
      phone=phone, 
      description=description, 
      user_id=user_id,
       )

    booking.save()

    # Send email
    send_mail(
       'Booking',
       'There has been an Booking for ' + partner + '. Sign into the admin panel for more info',
       'mfalme2030@gmail.com',
       [team_email, 'mfalme2030@gmail.com'],
       fail_silently=False
     )

    messages.success(request, 'Your request has been submitted, a team will get back to you soon')
    return redirect('/partners/'+partner_id)