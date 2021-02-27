from django.shortcuts import render, redirect
from app.models import File

# Create your views here.


def addFile(request):

    if request.method == 'POST':
        data = request.POST
        file = request.FILES.get('file')

        file = File.objects.create(
            description=data['description'],
            file=file,
        )
        return redirect('all_files')
    return render(request, 'app/upload.html')


def allFiles(request):
    files = File.objects.all()
    return render(request, 'app/all_files.html', {'files': files})
