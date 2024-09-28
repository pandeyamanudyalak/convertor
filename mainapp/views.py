# converter/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .models import Conversion
from PIL import Image
from io import BytesIO
import os
from django.conf import settings

# def convert_to_pdf(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             conversion = form.save()

#             # Convert image to PDF
#             image_path = conversion.image.path
#             pdf_path = os.path.splitext(image_path)[0] + '.pdf'
#             try:
#                 # Open and convert image to PDF
#                 image = Image.open(image_path)
#                 pdf_image = image.convert('RGB')
#                 pdf_image.save(pdf_path)
                
#                 # Update model instance with relative PDF file path
#                 conversion.pdf_file.name = os.path.relpath(pdf_path, settings.MEDIA_ROOT)
#                 conversion.save()
#             except Exception as e:
#                 print(f"Error converting image to PDF: {e}")
#                 return HttpResponse("Error converting image to PDF.", status=500)

#             return redirect('download', conversion.id)
#     else:
#         form = ImageUploadForm()
#     return render(request, 'index.html', {'form': form})



# from django.conf import settings
# import os

# def download_pdf(request, pk):
#     try:
#         conversion = Conversion.objects.get(pk=pk)
#         print('\n ➡ 50 conversion:', conversion)

#         if not conversion.pdf_file:
#             return HttpResponse("PDF file not found.", status=404)

#         # Construct file path using MEDIA_ROOT
#         file_path = os.path.join(settings.MEDIA_ROOT, conversion.pdf_file.name)
#         print('\n ➡ 56 file_path:', file_path)
        
#         if not os.path.exists(file_path):
#             print('-222222222222222222222222222222222-')
#             return HttpResponse("File does not exist on the server.", status=404)

#         # Serve the file for download
#         with open(file_path, 'rb') as pdf_file:
#             response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#             response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
#             return response
#     except Conversion.DoesNotExist:
#         return HttpResponse("Conversion record not found.", status=404)



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