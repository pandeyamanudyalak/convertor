# converter/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .models import Conversion
from PIL import Image
from io import BytesIO
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO




def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            conversion = form.save(commit=False)

            # Convert image to PDF
            image_file = request.FILES['image']
            image = Image.open(image_file)

            # Create a BytesIO object to hold the PDF data
            pdf_bytes = BytesIO()
            pdf_image = image.convert('RGB')
            pdf_image.save(pdf_bytes, format='PDF')
            pdf_bytes.seek(0)  # Rewind the BytesIO object to the beginning

            # Set the PDF file name
            pdf_filename = f"{os.path.splitext(image_file.name)[0]}.pdf"

            # Return the PDF as an HttpResponse
            response = HttpResponse(pdf_bytes.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
            return response

    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {'form': form})



def convert_to_pdf(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            conversion = form.save(commit=False)

            # Convert image to PDF
            image_file = request.FILES['image']
            image = Image.open(image_file)

            # Create a BytesIO object to hold the PDF data
            pdf_bytes = BytesIO()
            pdf_image = image.convert('RGB')
            pdf_image.save(pdf_bytes, format='PDF')
            pdf_bytes.seek(0)  # Rewind the BytesIO object to the beginning

            # Set the PDF file name
            pdf_filename = f"{os.path.splitext(image_file.name)[0]}.pdf"

            # Return the PDF as an HttpResponse
            response = HttpResponse(pdf_bytes.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
            return response

    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {'form': form})







def doc_to_pdf_view(request):
    if request.method == 'POST' and request.FILES['doc_file']:
        uploaded_file = request.FILES['doc_file']

        try:
            # Create an in-memory file for the PDF
            pdf_buffer = BytesIO()
            
            # Convert DOCX to PDF
            convert_docx_to_pdf(uploaded_file, pdf_buffer)

            # Return the PDF as a response
            pdf_buffer.seek(0)
            response = HttpResponse(pdf_buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="converted_file.pdf"'
            return response

        except Exception as e:
            return HttpResponse(f"Conversion failed: {str(e)}", status=500)

    return render(request, 'dic_to_pdf.html')

def convert_docx_to_pdf(input_file, pdf_buffer):
    doc = Document(input_file)

    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)

    width, height = letter
    x, y = 72, height - 72  

    for paragraph in doc.paragraphs:
        text = paragraph.text
        if y <= 72:  # Create a new page if we reach the bottom of the page
            pdf.showPage()
            y = height - 72 

        pdf.drawString(x, y, text)
        y -= 15  # Adjust line height

    pdf.save()


