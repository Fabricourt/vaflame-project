from django.shortcuts import render,  redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import BookingForm
from .models import Booking
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from.models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def booking(request):
    template ="booking.html"

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
    else:
       
        form = BookingForm()
        

     
    
    bookings = Booking.objects.order_by('-booking_date').filter(is_published=True)
    context ={
        'bookings':bookings,
        'form': form,
    }


    messages.success(request, 'Your booking has been recieved')
    return render (request,  template, context)

  





"""
@login_required
def booking(request):
  if request.method == 'POST':
   
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

    #  
  
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
    return redirect('/partners/'+partner_id)"""


   

