from django.shortcuts import render
from about_app.models import About, Vision, Term, News
from main_app.models import President
from event_app.models import CreateEvent
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def aboutUs(request):
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    pre = President.objects.all()
    abo = About.objects.all()
    context = {'abo': abo, 'pre': pre, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/about.html', context)

def vision(request):
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    pre = President.objects.all()
    vis = Vision.objects.all()
    context = {'vis': vis, 'pre': pre, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/vision.html', context)

def terms(request):
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    pre = President.objects.all()
    ter = Term.objects.all()
    context = {'ter': ter, 'pre': pre, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/terms.html', context)

def news(request):
    news = News.objects.filter(hide= False)
    paginator = Paginator(news,6)
    page_number = request.GET.get('page')
    try: 
        page_obj = paginator.get_page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    pre = President.objects.all()
    ter = Term.objects.all()
    context = {'news': news, 'page_obj': page_obj, 'pre': pre, 'ter': ter}
    return render(request, 'about_app/news.html', context)

def viewNews(request, pk): 
    view_news = News.objects.get(id= pk)
    eventor = CreateEvent.objects.all()
    news = News.objects.filter(hide = False) 
    context = {'view_news': view_news, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/viewnews.html', context) 