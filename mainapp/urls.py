from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('img-to-pdf', views.convert_to_pdf, name='convert_to_pdf'),
    path('doc-to-pdf', views.doc_to_pdf_view, name='doc_to_pdf'),
    path('word-to-pdf', views.doc_to_pdf_view, name='doc_to_pdf'),
    path('ppt-to-pdf', views.ppt_to_pdf_view, name='ppt_to_pdf'),
    path('excel-to-pdf', views.excel_to_pdf_view, name='excel_to_pdf'),
    path('html-to-pdf', views.html_to_pdf_view, name='html_to_pdf'),
    # path('upload', views.upload_pdf, name='upload_pdf'),
    path('pdf-editor', views.edit_pdf, name='edit_pdf'),
    path('download/<int:pk>', views.download_pdf, name='download_pdf'),
]