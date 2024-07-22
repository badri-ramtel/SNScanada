from django.shortcuts import render
from team_app.models import Year_Book, Committee, SubMenu

# Create your views here.
def team(request):
    teams = request.GET.get('member')
    if teams == None:
        community = Committee.objects.filter(year__current_year= True)
        years = Year_Book.objects.filter(current_year= True)
        quote = SubMenu.objects.filter(year__current_year= True)
    else:
        community = Committee.objects.filter(year__year_frame= teams)
        years = Year_Book.objects.filter(year_frame= teams)
        quote = SubMenu.objects.filter(year__year_frame= teams)
        
    committee = Year_Book.objects.all() 
    context = {'community': community, 'committee': committee, 'years': years, 'quote': quote}
    return render(request, 'team_app/committee.html', context) 

def viewCommittee(request, pk): 
    community = Committee.objects.get(id= pk)
    committee = Year_Book.objects.all() 
    context = {'community': community, 'committee': committee}
    return render(request, 'team_app/viewcommittee.html', context)
