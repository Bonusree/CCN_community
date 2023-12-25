from django.shortcuts import render
from .models import Notice
from academic.models import Department
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings
import os 
from CCN_community.decorators import superuser
# Create your views here.

@superuser
def add_notice(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        department = request.POST.get('department')
        pdf_file = request.FILES['pdf'] if 'pdf' in request.FILES else None

        if title and category and pdf_file :
            # Create a new Notice instance and save it to the database
            if department:
                dept_id = Department.objects.get(department=department)
                new_notice = Notice(
                    title=title,
                    category=category,
                    department=dept_id,
                    pdf=pdf_file
                )
            else:
                new_notice = Notice(
                    title=title,
                    category=category,
                    pdf=pdf_file
                )
            new_notice.save()
        notice(request)
    depts = Department.objects.all()
    return render(request,'add_notice.html',{"depts":depts})

def notice(request):
    notices = Notice.objects.all()
    context = {'notices':notices}
    return render(request,'notice.html',context)

@superuser
def delete_notice(request, notice_id):
    n = Notice.objects.filter(id=notice_id)
    n.delete()
    return notice(request)

def download_pdf(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)

    # Path to the PDF file
    file_path = os.path.join(settings.MEDIA_ROOT, str(notice.pdf))

    # Serve the file for download
    if os.path.exists(file_path):
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response

    # Handle if the file doesn't exist or other errors
    return HttpResponse("File not found", status=404)