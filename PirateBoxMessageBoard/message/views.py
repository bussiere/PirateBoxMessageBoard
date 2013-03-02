from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from message.forms import MessageForm
from message.models import Message,Configuration
# Create your views here.



def index(request,idm=None):
    nbrepost = 20
    try :
        conf = Configuration.objects.get(id__exact=1)
        nbrepost = conf.NbreMessage
    except :
        pass

    
    if request.method == 'POST':
        form = MessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            pseudo = form.cleaned_data['Pseudo']
            description = form.cleaned_data['Description']
            message = form.cleaned_data['Message']
            post = Message.objects.create(Description=description,Pseudo=pseudo,Message=message)
            post.save()
    if request.method == 'GET':
        if request.GET.get('idm'):
            idm = int(request.GET['idm'])
            print idm
    form = MessageForm() # An unbound form
    total = Message.objects.count()
    if idm == None or idm > total or idm < nbrepost :
        idm = total
    j = total + 444
    i = total
    while i < j :
        i = i +1
        post =  Message.objects.create(Description=i,Pseudo=i,Message=i)
        post.save()
    listemessage = Message.objects.filter(id__range=(idm-nbrepost+1,idm)).order_by('-id')
    supp = nbrepost + idm +1
    minus =  idm - nbrepost -1
    return render_to_response('index.html', {'form': form,'listemessage':listemessage,'idm':idm,'nbrepost':nbrepost,'total':total,'supp':supp,'minus':minus},RequestContext(request))


def message(request,idm=None):
    if idm == None :
        idm = 1
    else :
        idm = int(idm)
    if request.method == 'GET':
        if request.GET.get('idm'):
            idm = int(request.GET['idm'])
            print idm
    print idm
    try :
        message = Message.objects.get(id__exact=idm)
    except :
        idm = 1
        message = Message.objects.get(id__exact=idm)
    total = Message.objects.count()
    supp =  idm + 1
    minus =  idm  -1
    return render_to_response('message.html', {'message': message,'idm':idm,'total':total,'supp':supp,'minus':minus},RequestContext(request))

def my_404(request,idm=None):
    return redirect('http://10.0.0.1/')
