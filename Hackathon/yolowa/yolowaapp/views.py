from django.shortcuts import render, redirect, get_object_or_404
from .models import Yolowaapp
from django.utils import timezone
from .forms import YolowaappForm


# Create your views here.
def main(request):
    return render(request,'main.html')

def health(request):
    return render(request,'health.html')

def list(request):
    y_list=Yolowaapp.objects.all()
    return render(request, 'list.html', {'y_list':y_list})

def sub(request,id):
    y_sub=get_object_or_404(Yolowaapp, pk=id)
    return render(request, 'sub.html', {'y_sub':y_sub})

def americas(request):
    return render(request, 'Americas.html')

def asia(request):
    return render(request, 'Asia.html')

def southEastAsia(request):
    return render(request, 'southEastAsia.html')

def southPacific(request):
    return render(request, 'SouthPacific.html')

def europe(request):
    return render(request, 'Europe.html')

def travel(request):
    return render(request, 'travel.html')

def golf(request):
    return render(request, 'golf.html')

def culture(request):
    return render(request, 'culture.html')

def new(request):
    if request.method =='POST':
        yform = YolowaappForm(request.POST, request.FILES)
        if yform.is_valid():
            ycreate = yform.save(commit = False)
            ycreate.writer = request.user
            ycreate.pub_date = timezone.now()
            ycreate.save()
            return redirect('home')
    else:
        yform = YolowaappForm()
        return render(request, 'new.html', {'yform':yform})

def edit(request, id):
    y_edit= get_object_or_404(Yolowaapp, pk = id)
    if request.method == 'GET':
        y_form = YolowaappForm(instance = y_edit)
        return render(request, 'edit.html', {'y_edit':y_form})
    else:
        y_form = YolowaappForm(request.POST, request.FILES, instance = y_edit)
        if y_form.is_valid():
            y_edit = y_form.save(commit = False)
            y_edit.pub_date = timezone.now()
            y_edit.save()
        return redirect('home')

def delete(request, id):
    ydelete = Yolowaapp.objects.get(id = id)
    ydelete.delete()
    return redirect('home')

def explanation(request):
    return render(request, 'explanation.html')