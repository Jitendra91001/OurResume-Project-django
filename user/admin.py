from django.contrib import admin
from . models import profile,skill,contact,certificate,resume

# Register your models here.


class profileAdmin(admin.ModelAdmin):
    list_display=("ppic","name","dec")
admin.site.register(profile,profileAdmin)




class skillAdmin(admin.ModelAdmin):
    list_display=("pname","pdate")
admin.site.register(skill,skillAdmin)




class contactAdmin(admin.ModelAdmin):
    list_display = ("name","email","mobile","massage")
admin.site.register(contact, contactAdmin)





class resumeAdmin(admin.ModelAdmin):
    list_display = ("rpic","rdate")
admin.site.register(resume, resumeAdmin)





class certificateAdmin(admin.ModelAdmin):
    list_display = ("cpic","cname","rdate")
admin.site.register(certificate, certificateAdmin)
