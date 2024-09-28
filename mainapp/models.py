# converter/models.py

from django.db import models

class Conversion(models.Model):
    image = models.ImageField(upload_to='images/')
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
