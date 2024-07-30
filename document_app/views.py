from django.shortcuts import render, redirect
from event_app.models import CreateEvent
from document_app.models import Laws, References, Appreciations, Registrations, RegistrationInstruction, Program_Registrations
from about_app.models import News
from django.contrib import messages
import json

# Create your views here.
def lac(request):
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    docs = Laws.objects.filter(hide = False)
    context = {'eventor': eventor, 'docs': docs, 'news': news}
    return render(request, 'document_app/lac.html', context)


def reference(request):
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    docs = References.objects.filter(hide = False)
    context = {'eventor': eventor, 'docs': docs, 'news': news}
    return render(request, 'document_app/reference.html', context)

def appreciation(request):
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    docs = Appreciations.objects.filter(hide = False)
    context = {'eventor': eventor, 'docs': docs, 'news': news}
    return render(request, 'document_app/appreciation.html', context)

def register(request):
    if request.method == 'POST':
        your_name = request.POST.get('yname')
        age = request.POST.get('age')
        address = request.POST.get('address')
        city = request.POST.get('city')
        province = request.POST.get('province')
        postal_code = request.POST.get('pcode')
        your_contact = request.POST.get('contact')
        your_email = request.POST.get('yemail')
        parents_name = request.POST.get('pname')
        parents_contact = request.POST.get('pcontact[full]')
        parents_email = request.POST.get('pemail')
        program = request.POST.get('program')
        screenshot = request.FILES.get('screenshot')
        manual = request.FILES.get('manual')
        form = Program_Registrations(
            participant_full_name= your_name, 
            age= age, 
            address= address, 
            city= city, 
            province= province, 
            postal_code= postal_code,   
            your_contact= your_contact,
            your_email= your_email,
            parents_full_name= parents_name,
            parents_contact= parents_contact,
            parents_email = parents_email,
            program = program,
            screenshot= screenshot,
            manual= manual,
            )
        form.save()
        messages.success(request, 'SNS Family Thank you for registering!!!')
        return redirect('documentapp-register')
    
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    reg = Registrations.objects.filter(hide = False) 
    regs = request.GET.get('program')
    if regs == None:
        program = None  
    else:
        program = Registrations.objects.filter(f_name= regs) 
 
    ins = RegistrationInstruction.objects.all()
    with open('./static/files/all.json', encoding="utf8") as f:
        val = json.load(f)
    context = {'eventor': eventor, 'news': news, 'reg': reg, 'ins': ins, 'val': val, 'program': program}
    return render(request, 'document_app/program_registration.html', context)