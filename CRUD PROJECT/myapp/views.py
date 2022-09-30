import email
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,RedirectView,DetailView,FormView,View
from .models import StudentModel,UserModel
#from myapp.forms import StudentForm,UserForm
#from django.contrib.messages.viewsfrom django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.contrib import messages

# Create your views here.

class Create(CreateView,SuccessMessageMixin):
      template_name='myapp/create.html'
      model=StudentModel
      #form=StudentForm
      fields="__all__"
      success_url='/create/'
      success_sessages='Student Details Are Saved'

class Show(ListView):
      template_name='myapp/show.html'
      model=StudentModel

class Update(UpdateView):
      template_name='myapp/update.html'
      model=StudentModel
      fields="__all__"  
      success_url='/show/' 

class Delete(DeleteView):
      template_name='myapp/delete.html'
      model=StudentModel
      fields="__all__"
      success_url='/show/'  

class Material(RedirectView):
      url='https://www.djangoproject.com'  

class Single(DetailView):
      template_name='myapp/details.html'
      model=StudentModel
      fields="__all__"     
      success_url='/show/'    

class Formdata(FormView):
      template_name='myapp/form.html'
      #model=UserModel
      #fields='__all__'
      form_class=UserForm
      success_url='/main/'

class Validate(View):
      def post(self,request):
            na=request.POST.get('s1')
            emi=request.POST.get('s2')
            try:
                  data=StudentModel.objects.get(name=na,email=emi)
                  #messages.success(request,'login successfully')
                  return render(request,'myapp/validate.html',{"data":data})
                  #return redirect('show')
                  
                  

            except StudentModel.DoesNotExist:
                  messages.error(request,'Invalid Name And Emailid')
                  return redirect('login')
                    



