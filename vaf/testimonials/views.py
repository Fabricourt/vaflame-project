from django.shortcuts import render,  redirect
from django.contrib import messages
from .forms import TestimonialForm
from .models import Testimonial
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from.models import Testimonial
from django.contrib.auth.decorators import login_required


@login_required
def testimonial(request):
    template ="testimonial.html"

    if request.method == "POST":
        form = TestimonialForm(request.POST)

        if form.is_valid():
            form.save()
    else:
       
        form = TestimonialForm()
        

    testimonials = Testimonial.objects.order_by('-date_posted').filter(is_published=True)
    context ={
        'testimonials':testimonials,
        'form': form,
    }


    messages.success(request, 'Your testimony has been recieved')
    return render (request,  template, context)

  






   

