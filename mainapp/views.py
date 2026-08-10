from django.shortcuts import render, redirect  # 👈 redirect import cheyyanam
from django.contrib import messages
from .forms import EnquiryForm

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def services(request):
    services_list = [
        {'name': 'Visa Assistance', 'icon': 'fa-passport', 'desc': 'Tourist, Business, Student, Work visas'},
        {'name': 'Passport Services', 'icon': 'fa-id-card', 'desc': 'New, Renewal, Tatkal, Minor passport'},
        {'name': 'Ticket Booking', 'icon': 'fa-plane', 'desc': 'Domestic & International flights'},
        {'name': 'Travel Insurance', 'icon': 'fa-shield-alt', 'desc': 'Comprehensive travel coverage'},
        {'name': 'Forex Exchange', 'icon': 'fa-money-bill-wave', 'desc': 'Best exchange rates'},
        {'name': 'Holiday Packages', 'icon': 'fa-umbrella-beach', 'desc': 'Customized tour packages'},
    ]
    return render(request, 'mainapp/services.html', {'services': services_list})

def locations(request):
    branches = [
        {'name': 'Head Office', 'address': 'CMS Travels & Solutions, Kochi, Kerala', 'phone': '+91 9876543210'},
        {'name': 'Branch Office', 'address': 'CMS Travels & Solutions, Trivandrum, Kerala', 'phone': '+91 9876543211'},
    ]
    return render(request, 'mainapp/locations.html', {'branches': branches})

def gallery(request):
    return render(request, 'mainapp/gallery.html')

def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We will contact you soon.')
            return redirect('contact')  # 👈 Now redirect works!
    else:
        form = EnquiryForm()
    return render(request, 'mainapp/contact.html', {'form': form})