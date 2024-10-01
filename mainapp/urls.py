# converter/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('img-to-pdf', views.convert_to_pdf, name='convert_to_pdf'),
    path('doc-to-pdf', views.doc_to_pdf_view, name='doc_to_pdf')
]
