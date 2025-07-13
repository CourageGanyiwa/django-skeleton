from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    members_list = Member.objects.all()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': members_list,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = Member.objects.all().values('id','first_name', 'last_name', 'phone', 'joined_date')
    template = loader.get_template('template.html')    
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context,request))