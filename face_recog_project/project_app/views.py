from fpdf import FPDF
import base64
import cv2
import os
import shutil
import re
import mimetypes
import PyPDF2
import io
from io import BytesIO
from urllib.request import urlopen
from unicodedata import name

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings
from django.db import IntegrityError
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers

from PIL import Image
from imageio import imread

from project_app.forms import UserImageForm, web_photo, UrlForm, NewUserForm, UserRegistrationForm, SignUpForm
from project_app.models import Person, UploadImage, WebImage, MultipleImage, GetUrl, Download
from project_app.face_recog_file import recognize
from project_app.tokens import account_activation_token







def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def about_view(request):
	return render(request, 'about.html')

def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
            photo_name = img_object.image.name
            split_name = photo_name.split('/')
            corected_name = split_name[1]
              
            return render(request, 'input.html', {'form': form, 'img_obj': img_object, 'image_name': corected_name})  
    else:  
        folder = os.path.join(settings.MEDIA_ROOT,'images')
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                error = "could no find directory"
        folder1 = os.path.join(settings.MEDIA_ROOT,'folder')
        for filename in os.listdir(folder1):
            file_path = os.path.join(folder1, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                error = "could no find directory"
        form = UserImageForm()  
    return render(request, 'input.html', {'form': form})  



def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            a =  MultipleImage.objects.create(images=image)
            a.save 
    images = MultipleImage.objects.all()

    return render(request, 'Info_page.html', {'images': images})



def image_web(request):  
    if request.method == 'POST': 
        form = UrlForm(request.POST, request.FILES)
        if form.is_valid():  
            dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
            ImageData1 = request.POST.get('Url')
            
            print(ImageData1)
            img = imread(io.BytesIO(base64.b64decode(ImageData1 + '=')))
            ImageData = dataUrlPattern.match(ImageData1).group(2)
            if (ImageData == None or len(ImageData) == 0):
                # PRINT ERROR MESSAGE HERE
                pass


            
            image = WebImage.objects.create(img)
            image.save
            # Decode the 64 bit string into 32 bit
            ImageData = base64.b64decode(ImageData)
           
            _format, _img_str = ImageData1.split(';base64,')
            _name, ext = _format.split('/')
            
            final = ContentFile(base64.b64decode(_img_str))

            for index, image in enumerate(ImageData):
                
                # https://stackoverflow.com/a/6966225/15164646
                final_image = Image.open(BytesIO(base64.b64decode(str(image))))

                    # https://www.educative.io/edpresso/absolute-vs-relative-path
                    # https://stackoverflow.com/a/31434485/15164646
                
            
           
  


            # Getting the current instance object to display in the template  
            img_object = form.instance 
              
            return render(request, 'Info_page.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
    return render(request, 'Info_page.html', {'form': form})  



def image_webw(request):  
    context = dict()
    if request.method == 'POST':
       
        path = ""  # src is the name of input attribute in your html file, this src value is set in javascript code
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        if image is not None:
            obj = image_web.objects.create(image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored in my server/local device
        else :
            return redirect('/')
        return redirect('any_url')
    return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.         
def add_picture(request):
    data = {}
    form = UserImageForm()
    if request.method == "POST":
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['picture_form'] = render_to_string("test.html", 
                                               {'form': form}, request=request)

    data['picture_form'] = render_to_string("test.html",
                                               {'form': form}, request=request)
    return JsonResponse(data)



def edit_picture(request, id):
    data = {}
    image = get_object_or_404(UploadImage, pk=id)
    form = UserImageForm(instance=image)
    if request.method == "POST":
        form = UserImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['edit_picture'] = render_to_string("test.html", 
                                                {'form': form}, request=request)

    data['edit_picture'] = render_to_string("test.html", 
                                                {'form': form}, request=request)
    return JsonResponse(data)


def test(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'test.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'test.html', {'form': form})  


def delete_book(request, ):
    folder = os.path.join(settings.MEDIA_ROOT,'images')
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            error = "could no find directory"
    form = UserImageForm()  
    form = UserImageForm()  
    return render(request, 'input.html', {'form': form})
   
#empties a folder
def empty_folder(folder_name):
    folder = os.path.join(folder_name)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            error = "could no find directory"
    folder1 = os.path.join(settings.MEDIA_ROOT,'folder')
    for filename in os.listdir(folder1):
        file_path = os.path.join(folder1, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            error = "could no find directory"



def Info_page(request):
    id = 7
    empty_folder('download')
    #calling face_recog_file to get id of recognized person
    id = int(id)

    x = 0
    while x<6 :
        print(id)
        x += 1
    ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #store name of all objects of Person class in a list
    person_object = []
    persons = Person.objects.all()
    for obj in persons:
        print(obj)
        person_object.append(obj)
    print(person_object)
    

    detected_person = person_object[id]
    #get photo name
    photo_name = detected_person.Photo.name
    #take away folder name
    split_name = photo_name.split('/')
    corected_name = split_name[1]





    #Store info about selected object in pdf
    pdf_w=210
    pdf_h=297
    class PDF(FPDF):
        def lines(self):
            self.rect(5.0, 5.0, 200.0,287.0)
            self.rect(8.0, 8.0, 194.0,282.0)
        def titles(self):
            self.set_xy(0.0,0.0)
            self.set_font('Arial', 'B', 25)
            self.set_text_color(0, 0, 0)
            self.cell(w=210.0, h=40.0, align='C', txt="Information About: ", border=0)
        def text(self, text,x, y, font, align):
            self.set_xy(x,y)
            self.set_font('Arial', 'B', font)
            self.set_text_color(0, 0, 0)
            self.cell(w=210.0, h= 40.0, align=align, txt=text, border=0)
        def imagex(self, url, w, h, x, y):
            self.set_xy(x, y)
            self.image(url,  link='', type='', w=w, h=h)


    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.lines()
    pdf.titles()

    fields = ['Name : ', 'School : ', 'Department : ', 'Email : ', 'Address : ', 'Contact : ']
    field = ['Name', 'School', 'Department', 'Email', 'Address', 'Contact']
    pdf.imagex('.'+detected_person.Photo.url, 65, 70, 72.5,40)
    h = 125
    for i in range(0, len(fields)):
        print(field[i])
        text = fields[i] + getattr(detected_person, field[i])
        print(text)
        pdf.text(text,30, h, 18, 'L')
        h += 10

    pdf.text('By',0.0, 220, 20, 'C')
    pdf.imagex('./media/Personal_tof/face-scan.png', 13, 13, 70,248)
    pdf.text('FaceGenuis',0.0, 235, 20, 'C')


    pdf.output('download/Records.pdf','F').encode('latin-1')
    a =  Download.objects.create(file='download/Records.pdf')
    a.save
    pdf = Download.objects.all()




    
    return render(request, 'Info_page.html', {'Person': detected_person, 'image_name': corected_name, 'id': id, 'pdf': pdf})


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'Records.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/download/' + filename
    # Open the file for reading content
    path = open(filepath, 'r', encoding = 'latin-1')
    
    
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def multiple_image_view(request):
    id_list = recognize()
    if len(id_list) == 1:
        Info_page(request, id_list[0])
    elif len(id_list) > 1:
        
        
        Info_page(request, id_list[0])
        ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        #store name of all objects of Person class in a list
        person_object = []
        persons = Person.objects.all()
        for obj in persons:
            print(obj)
            person_object.append(obj)
        print(person_object)
        detected_persons = []
        corected_names = []
       
        for id in id_list:
            detected_persons.append(person_object[id])
        #get photo name
            photo_name = person_object[id].Photo.name
        #take away folder name
            split_names = photo_name.split('/')
            corected_names.append(split_names[1])

        return render(request, 'multiple_image_view.html', {'image_name': corected_names})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, '/register.html', context)



def send_activation_email(user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    activation_url = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
    
    subject = 'Please Activate Your Account'
    message = f'Hi {user.username},\n\nPlease click the following link to confirm your registration:\n\n{activation_url}'
    from_email = 'webmaster@localhost'
    to_email = user.email
    send_mail(subject, message, from_email, [to_email])

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'activation_invalid.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return render(request, 'activation_sent.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def activation_sent_view(request):
    return render(request, 'activation_sent.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)


        providers = get_providers()
        # Get Google provider object
        google_provider = None
        for provider in providers:
            if provider.id == 'google':
                google_provider = provider

    # Get the Google app ID and key from SocialApp model
        if google_provider:
            google_app = SocialApp.objects.get(provider='google')
            google_app_id = google_app.client_id
            google_app_key = google_app.secret
        return render(request, 'myfirst.html', {
        'google_app_id': google_app_id,
        'google_app_key': google_app_key
        })
        if user is not None:
            login(request, user)
            return redirect('index')
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


class MyPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'