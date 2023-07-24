from django.contrib import admin
from .models import StudentSubjectsScore, Subjects, Personnel, Classes, Schools, SchoolStructure

# Register your models here.
admin.site.register(StudentSubjectsScore)
admin.site.register(Subjects)
admin.site.register(Personnel)
admin.site.register(Classes)
admin.site.register(Schools)
admin.site.register(SchoolStructure)