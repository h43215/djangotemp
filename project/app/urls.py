from django.urls import path
from . import views

urlpatterns = [
    path('viewcontact/',views.viewcontact,name = "viewcontact"),
    path('contact/',views.contact,name = "contact"),
    path('editcontact/',views.Editcontact,name="editcontact"),
    path('Deletecontact/', views.Deletecontact,name ="Deletecontact"),
    path('Edit/',views.Edit,name="Edit"),
    path('contactcode/',views.contactcode,name="contactcode"),
]