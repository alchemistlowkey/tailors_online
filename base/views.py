from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactFormEntry


def home(request):
    return render(request, 'base/home.html')


def product(request):
     return render(request, 'base/product.html')


def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')

        # Save form data to the database
        ContactFormEntry.objects.create(name=name, email=email, comments=comments)

        # You can add further actions like sending emails, displaying a thank you message, etc.
        messages.success(request, f'Thank you {name} for contacting Tailors Online')
        return redirect('base-home')  # Redirect to a success page after form submission

    return render(request, 'contactform/contact_form.html')
