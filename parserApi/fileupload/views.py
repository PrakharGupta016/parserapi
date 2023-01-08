from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .forms import MyFileUploadForm
from .models import file_upload
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pyresparser import ResumeParser
# Create your views here.
@api_view(['POST'])
def index(request):
    if request.method == 'POST':
        c_form  = MyFileUploadForm(request.POST,request.FILES)
        if c_form.is_valid():
                name = c_form.cleaned_data['file_name']
                files_store = c_form.cleaned_data['files_data']
                file_upload(file_name1 =name, my_file=files_store).save()

                data = ResumeParser(f"media/{files_store}").get_extracted_data()
                print(files_store)
                return Response(data)
        else:
            print(c_form.errors)
            return Response("error") 

    else:
        context ={
            'form':MyFileUploadForm()
        }
        return render(request,'index.html',context)
