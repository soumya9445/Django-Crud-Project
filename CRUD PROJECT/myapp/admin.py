from django.contrib import admin
from myapp.models import StudentModel

# Register your models here.
@admin.register(StudentModel)

class StudentAdmin(admin.ModelAdmin):
      list_display=['name','contact','email','course','gender','image']
