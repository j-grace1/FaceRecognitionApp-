from fpdf import FPDF
import imp
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from project_app.forms import UserImageForm , web_photo,UrlForm
from .face_recog_file import recognize
from .models import Person, UploadImage, WebImage, MultipleImage, GetUrl, Download
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
import re
import base64
from django.urls import reverse_lazy
import os, shutil
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
from io import BytesIO
import PIL.Image as Image
import io
import cv2
from imageio import imread
import mimetypes, PyPDF2





def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


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
    empty_folder('download')
    #calling face_recog_file to get id of recognized person
    id = recognize()
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
    
