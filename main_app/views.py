from django.shortcuts import render
from main_app.models import Slider, President, PresidentMessage, Subscribe, Advertise
from about_app.models import About, News
from gallery_app.models import Category, Photo
from event_app.models import CreateEvent
from document_app.models import Registrations
from django.http import JsonResponse

# Create your views here.
def home(request):
    slide = Slider.objects.all()
    count = Slider.objects.all().count()
    counter = range(count)
    about = About.objects.all()
    pre = President.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('category')
    if cat == None:
        photos = Photo.objects.all()
        cat_photos = list(photos) 
    else:
        photos = Photo.objects.filter(category__name= cat) 
        cat_photos = list(photos)
        data = list(photos.values()) 
        return JsonResponse(data, safe= False) 

    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    program = Registrations.objects.filter(hide = False) 
    adv = request.GET.get('advertise')
    if adv == None:
        ads = Advertise.objects.all() 
    else:
        ads = Advertise.objects.filter(content__id= adv)  
    context = {'slide': slide, 'counter': counter, 'about': about, 'pre': pre, 'categories': categories, 'eventor': eventor, 'news': news, 'program': program, 'ads': ads, 'photos': photos}
    return render(request, 'main_app/home.html', context) 
    

def president(request):
    president = President.objects.all()
    message = PresidentMessage.objects.all()
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    context = {'president': president, 'message': message, 'eventor': eventor, 'news': news}
    return render(request, 'main_app/president.html', context)
 

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        form = Subscribe(email= email)
        form.save()
        # success = 'SNS Family Thank you for Subscribe!!!'
        return JsonResponse({'success': True})

    
def advertise(request, pk):
    adv = Advertise.objects.get(id= pk)
    adv_ids = list(Advertise.objects.values_list('id', flat= True))
    current_index= adv_ids.index(int(pk))
    try:
        next = adv_ids[current_index - 1]
        prev = adv_ids[current_index + 1]
    except IndexError:
        next = adv_ids[int(len(adv_ids)) - 2] 
        prev = adv_ids[0]

    advertise = Advertise.objects.all()
    context = {'adv': adv, 'next': next, 'prev': prev, 'advertise': advertise} 
    return render(request, 'main_app/advertise.html', context)