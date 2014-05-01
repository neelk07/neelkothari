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

#default landing page --> may remove to have my blog become the front page of neelkothari.com
def landing_page(request):

	variables = RequestContext(request, {

	})
	return render_to_response('landing.html',variables)

#front page for blog
def blog(request):
	posts = Post.objects.order_by('-created')[:3]
	variables = RequestContext(request, {
		'posts': posts,
		})
	return render_to_response('blog.html', variables)

#extended page if people want to see all my posts
def blog_extended(request):
	posts = Post.objects.order_by('-created')
	variables = RequestContext(request, {
			'posts':posts,
		})

#just basic information about myself and my projects
def profile(request):
	variables = RequestContext(request, {

	})
	return render_to_response('projects.html',variables)

#uploading covers and other musical creations
def music(request):

	variables = RequestContext(request, {

	})
	return render_to_response('music.html',variables)

#landing page for budge 
def budge(request):
        
        variables = RequestContext(request, {
          })
        return render_to_response('budge.html', variables)

#supposed to be my visualizing literature projects    
def hp(request):
        
        variables = RequestContext(request, {
          })
        return render_to_response('hp_steamgraph.html', variables)
