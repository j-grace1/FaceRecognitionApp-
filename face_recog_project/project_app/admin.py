from django.contrib import admin

# Register your models here.


from .models import Person, UploadImage, MultipleImage, WebImage, GetUrl, Download
admin.site.register(Person)
admin.site.register(UploadImage)
admin.site.register(MultipleImage)
admin.site.register(WebImage)
admin.site.register(GetUrl)
admin.site.register(Download)
