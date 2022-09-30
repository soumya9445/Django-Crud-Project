from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from myapp import views
from django.conf.urls.static import static
from classbased import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',TemplateView.as_view(template_name='index.html'),name='main'),
    path('create/',views.Create.as_view(),name='create'),
    path('show/',views.Show.as_view(),name='show'),
    path('update/<int:pk>',views.Update.as_view(),name='update'),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),
    path('material/',views.Material.as_view(),name='material'),
    path('single/<int:pk>',views.Single.as_view(),name='single'),
    path('form_data/',views.Formdata.as_view(),name='form_data'),
    path('login/',TemplateView.as_view(template_name='myapp/login.html'),name='login'),
    path('validate/',views.Validate.as_view(),name='validate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)