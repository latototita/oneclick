from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *

# defining function
def index(request):
    # checking whether request.method is post or not
    movies=File.objects.all()
    if request.method == 'POST':
        return render(request, 'index.html')
    context={'movies':movies}
    return render(request, 'index.html',context)


def download(request, path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404
