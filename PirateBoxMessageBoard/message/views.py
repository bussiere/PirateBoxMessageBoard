from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from message.forms import MessageForm
from message.models import Message
# Create your views here.



def index(request):
    if request.method == 'POST':
    	form = MessageForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            pseudo = form.cleaned_data['Pseudo']
            description = form.cleaned_data['Description']
            message = form.cleaned_data['Message']
            post = Message.objects.create(Description=description,Pseudo=pseudo,Message=message)
            post.save()
    form = MessageForm() # An unbound form
    listemessage = Message.objects.values('id').order_by('-id')[:10]

    return render_to_response('index.html', {'form': form,'listemessage':listemessage},RequestContext(request))


def id(request):
	pass