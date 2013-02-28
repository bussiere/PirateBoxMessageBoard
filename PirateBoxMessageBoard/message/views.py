from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from message.forms import MessageForm

# Create your views here.



def index(request):
    if request.method == 'POST':
    	pass

    else:
    	pass
    form = MessageForm() # An unbound form

    return render_to_response('index.html', {'form': form},RequestContext(request))

   