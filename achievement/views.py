from django.shortcuts import render,redirect
from .models import Achievement
from CCN_community.decorators import superuser

# Create your views here.
def achievement(request):
    achievements = Achievement.objects.all()
    return render(request,'achievement.html',{'achievements':achievements})

@superuser
def add_achievement(request):
    if request.method=="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date_achieved = request.POST.get('date_achieved')
        image = request.FILES.get('image')  # Get uploaded image file

        # Create a new Achievement instance
        new_achievement = Achievement.objects.create(
            title=title,
            description=description,
            date_achieved=date_achieved,
            image=image
        )
        # Optionally, you might want to save the instance to the database
        new_achievement.save()
        return redirect('achievement')
    return render(request,'add_achievement.html')

@superuser
def delete_achievement(request, ach_id):
    if ach_id:
        ach = Achievement.objects.get(id=ach_id)
        ach.delete()
    return redirect('achievement')
    