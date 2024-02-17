# views.py

from .models import UploadedFile
from django.shortcuts import redirect, render

def index(request):
    if request.method == 'POST' and request.FILES['pdfFile']:
        pdf_file = request.FILES['pdfFile']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        uploaded_file_url = fs.url(filename)
        
        # Save file information to the database
        uploaded_file = UploadedFile.objects.create(name=pdf_file.name, file_path=uploaded_file_url)
        
        # Print the file path for verification
        print("File path:", fs.path(filename))
        
        return render(request, 'index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'index.html')
