from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import Profile

# Temporary storage for OTPs (better to store in DB)
otp_storage = {}

@login_required(login_url='login')
def dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.phone_number = request.POST.get('phone_number')

        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']

        profile.save()
        return redirect('dashboard')  # refresh page to show updated data

    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'dashboard.html', context)


def SignupPage(request):
    error_message = None  # default no error
    email_message = None  # default no error
    data ={
            'email_message':email_message,
            'error_message':error_message
        }

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            error_message = "Your password and confirm password are not the same!!"

        else:
            if User.objects.filter(username=uname).exists():
                return HttpResponse("Username already taken!")
            if User.objects.filter(email=email).exists():
                email_message = "Your password and confirm password are not the same!!"

            # Create inactive user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.is_active = False   # User will be active after OTP verification
            my_user.save()

            # Generate OTP
            otp = str(random.randint(100000, 999999))
            otp_storage[my_user.username] = otp

            # Send OTP to email
            send_mail(
                "Verify your Email",
                f"Your OTP is {otp}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            # Redirect to OTP verification page
            request.session['username'] = uname
            return redirect('verify_email')
        

    return render(request, 'signup.html', data)


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def VerifyEmailPage(request):
    username = request.session.get('username')
    if not username:
        return redirect('signup')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        correct_otp = otp_storage.get(username)

        if entered_otp == correct_otp:
            # Activate user
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()

            # Remove OTP after verification
            del otp_storage[username]

            return render(request, 'verify_email.html', {
                'success_message': "✅ Email verified successfully! Now you can login."
            })
        else:
            return render(request, 'verify_email.html', {
                'otp_error': "❌ Invalid OTP. Try again!"
            })

    return render(request, 'verify_email.html')
