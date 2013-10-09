# Create your views here.
from django.http import HttpResponse
from guestbook.models import GueatBookNew
from django.shortcuts import render_to_response
from forms import GuestBookForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def hello(request):
    name="pavani"
    html="<html><body>Hi %s. this seems to work</body></html>"%name
    return HttpResponse(html)

def success(request):
    html="<html><body><a href='/guestbookdetails/all'>View Previous Signed In Users </a></body></html>"
    return HttpResponse(html)
def guestbookdetails(request):
    return render_to_response('guestbookdetails.html',
                              {'guestbookdetails':GueatBookNew.objects.all()})
def guestbook(request,guestbook_id):
    return render_to_response('guestbook.html',
                             {'guestbook': 
                              GueatBookNew.objects.get(id=guestbook_id)})

def create(request):
    if request.POST:
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
        
            return HttpResponseRedirect('/guestbookdetails/success')
    else:
        form = GuestBookForm()
    args = {}
    args.update(csrf(request))

    args[ 'form' ] = form
    
    return render_to_response('create_guestbook.html',args)
        
    args = {}
    args.update(crsf(request))

    args['form'] = form

    return render_to_response('create_guestbook.html',args)
