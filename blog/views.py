from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from datetime import datetime, timedelta
from django.db.models import Q


def landing_page(request):

	variables = RequestContext(request, {

	})
	return render_to_response('landing.html',variables)

def blog(request):
	posts = Post.objects.order_by('-created')
	variables = RequestContext(request, {
		'posts': posts,
		})
	return render_to_response('blog.html', variables)

def profile(request):
	variables = RequestContext(request, {

	})
	return render_to_response('projects.html',variables)

def music(request):

	variables = RequestContext(request, {

	})
	return render_to_response('music.html',variables)
 
def budge(request):
        
        variables = RequestContext(request, {
          })
        return render_to_response('budge.html', variables)
