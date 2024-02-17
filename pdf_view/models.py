from django.db import models

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)  # Or use FileField if you want to store file paths
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'pdf_view'
