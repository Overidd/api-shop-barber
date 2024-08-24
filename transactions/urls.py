from django.urls import path
from .views import *

urlpatterns = [
   path('appointment/', AppointmentCreateView.as_view()),
   path('appointment/list/', AppointmentView.as_view()),

   path('payment/list/', PaymentListView.as_view()),
   path('payment/create/', PaymentCreateView.as_view()),
   path('payment/update/<int:pk>/', PaymentUpdateView.as_view()),
   path('payment/delete/<int:pk>/', PaymentDestroyView.as_view()),
   path('payment/notifications/', PaymentNotificationView.as_view()),

   path('invoice/create/<int:appointment_id>/', InvoiceCreateView.as_view()),
   path('invoice/find/<int:tipo_de_comprobante>/<str:serie>/<int:numero>/', InvoiceRetrieveView.as_view()),

]