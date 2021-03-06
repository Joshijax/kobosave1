from django.shortcuts import render
from allauth.account.views import SignupView as AllAuthSignupView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProfileUploadForm
from .models import ProfilPicx
from django.contrib.auth.models import User
from django.contrib import messages 
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse
# Create your views here.




def index(request):
    
    return render(request, 'index.html',)

def our_Solution(request):
    
    return render(request, 'our Solutions.html',)

 
def Who(request):
    
    return render(request, 'Who we are.html',)



def contact(request):
    
    return render(request, 'contact us.html',)

@login_required(login_url='/')
def dashboard(request):
    
    return render(request, 'payment.html',)

@login_required(login_url='/')
def orders(request):
    
    return render(request, 'orders.html',)

@login_required(login_url='/')
def profile(request):
    print(request.method)
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        
        if settings.USE_S3:
            obj = User.objects.get(id=request.user.id)
            profile = obj.profilePicx
            profile.img = image_file
            profile.save()
            # upload = ProfilPicx(user= request.user, img=image_file)
            # upload.save()
            # image_url = upload.img.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            return render(request, 'upload.html', {
                'image_url': image_url
            })
        return redirect(reverse('profile'))
    
    return render(request, 'my profile.html',)

def upload_profilePicx(request, user_id):
    

    if request.user.is_authenticated == True:
        user = request.user
        print(user)
       
        tests = ProfilPicx.objects.get(user_id = user_id,)
        tests.delete()
        if request.method == 'POST':
            obj = User.objects.get(id=user_id)
            form = ProfileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                obj = User.objects.get(id=user_id)
                profile = obj.profilePicx
                profile.img = form.cleaned_data['img']
                profile.save()
                
            print('N')
            messages.add_message(request, messages.SUCCESS, 'Profile Picx Uploaded')

def logout_request(request):
    logout(request)
    return redirect('/')


def handler404(request, exception):   
    return redirect('/')