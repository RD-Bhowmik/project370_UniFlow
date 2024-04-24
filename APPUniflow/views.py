from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import Group, User
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth import authenticate,login,logout
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.


def mainhome(request):

    return render(request, 'index.html')

def afterLogin(request):

    return render(request, 'home.html')

#user register function
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()


            username = form.cleaned_data.get("username")


            messages.success(request,"Account was created for " +username)
            return redirect("login")
        
    
    context={"form":form}
    return render(request,"register.html",context)

#user register function end ------


#user login & logut function
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user= authenticate(request, username =username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")
        
        context={}
        return render(request,"login.html",context)



def logoutUser(request):
    logout(request)
    #return redirect("login")
    return render(request,"index.html")





@login_required(login_url="login")
def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Donor.objects.filter(email=email).exists():
                return render(request, 'blood_donors/donor_exists.html')
            else:
            
                form.save()
                return redirect('donor_added')
    else:
        form = DonorForm()
    return render(request, 'add_donor.html', {'form': form})


def donor_added(request):
    return render(request, 'doner_added.html')


# def donor_list(request):
#     donors = Donor.objects.all()
#     return render(request, 'donor_list.html', {'donors': donors})

def donor_list(request):
    blood_group = request.GET.get('blood_group')

    address = request.GET.get('address')

    donor_count = Donor.objects.count()
    donors = Donor.objects.all()
    blood_type_counts = Donor.objects.values('blood_type').annotate(count=Count('blood_type'))


    if blood_group:
        donors = Donor.objects.filter(blood_type=blood_group)
    
    if address:
        donors = donors.filter(address__icontains=address)

    return render(request, 'donor_list.html', {'donors': donors, 'donor_count': donor_count , 'blood_type_counts': blood_type_counts})



def register_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = HospitalForm()
    return render(request, 'reghospital.html', {'form': form})



def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to event list page after adding event
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to event list page after updating event
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('event_list')  # Redirect to event list page after deleting event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})



# def add_blood_request(request):
#     if request.method == 'POST':
#         form = BloodRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Redirect to home page after successful request submission
#     else:
#         form = BloodRequestForm()
#     return render(request, 'add_flood_request.html', {'form': form})

def add_blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood_request_list')  # Redirect to the blood request list page after successful submission
    else:
        form = BloodRequestForm()
    return render(request, 'add_flood_request.html', {'form': form})


def blood_request_list(request):
    # Query all blood requests from the database
    requests = BloodRequest.objects.all()

    # Pass the blood requests to the template for rendering
    return render(request, 'blood_request_list.html', {'requests': requests})



# Function to update a blood request
def update_blood_request(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)
    if request.method == 'POST':
        form = BloodRequestForm(request.POST, instance=blood_request)
        if form.is_valid():
            form.save()
            return redirect('blood_request_list')  # Redirect to the blood request list page after successful update
    else:
        form = BloodRequestForm(instance=blood_request)
    return render(request, 'update_blood_request.html', {'form': form})

# Function to delete a blood request
def delete_blood_request(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)
    if request.method == 'POST':
        blood_request.delete()
        return redirect('blood_request_list')  # Redirect to the blood request list page after successful deletion
    return render(request, 'delete_blood_request.html', {'blood_request': blood_request})

def adminPannel(request):

    return render(request, 'admin_pannel.html')