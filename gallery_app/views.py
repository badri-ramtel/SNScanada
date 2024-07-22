from django.shortcuts import render
from .models import Category, Photo
from team_app.models import Year_Book
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def gallery(request):
    category_ids = Category.objects.values_list('id', flat=True)
    categories_new = []
    for category_id in category_ids:
        categories = Category.objects.get(id= category_id)
        first_photo = categories.photo_set.first()
        photo_count = categories.photo_set.count()
        categories_new.append({
            'categories': categories,
            'first_photo': first_photo,
            'photo_count': photo_count
        }) 
          
    photos = Photo.objects.all()
    committee = Year_Book.objects.all()
    context = {'categories_new': categories_new, 'committee': committee, 'photos': photos}
    return render(request, 'gallery_app/gallery.html', context)   

def gridView(request, pk):
    grid_categories = Category.objects.get(id= pk)
    grid_images = Photo.objects.filter(category= pk)
    paginator = Paginator(grid_images, 12)
    page_number = request.GET.get('page')
    try: 
        page_obj = paginator.get_page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    context = {'grid_categories': grid_categories, 'grid_images': grid_images, 'page_obj': page_obj, 'categories': categories}
    return render(request, 'gallery_app/gridview.html', context)


def viewPhoto(request, grid_id, pk):
    grid = Category.objects.get(id= grid_id)
    photo = Photo.objects.get(id= pk)
    photo_ids = list(Photo.objects.values_list('id', flat= True).filter(category= grid_id))
    current_index= photo_ids.index(int(pk))
    try:
        next = photo_ids[current_index - 1]
        prev = photo_ids[current_index + 1]
    except IndexError:
        next = photo_ids[int(len(photo_ids)) - 2]
        prev = photo_ids[0]
    picture = Photo.objects.filter(category= grid_id) 
    committee = Year_Book.objects.all()
    context = {'grid': grid, 'photo': photo, 'picture': picture, 'committee': committee, 'next': next, 'prev': prev}
    return render(request, 'gallery_app/viewphoto.html', context) 
