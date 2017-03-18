from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import User, Venue, Reviews, Pics, Cuisines #Memo, Facilities, Suitable, SpaceType
from .forms import VenueFilter, ReviewForm
import django_filters

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

#def show(request, id=None, name=None):
#	name = name.replace('-',' ')
#	instance = get_object_or_404(Venue, id=id)
#	if(instance.name == name):
#		reviews = Reviews.objects.filter(venue__id = instance.id)
#		context = {
#			"instance" : instance,
#			"title" : instance.name,
#			"reviews" : reviews,
#		}
#		return render(request, "detail.html", context)
#	else:
#		return HttpResponseNotFound('<h1>Page not found</h1>')


def ocazion(request):
	return render(request,"ocazion.html")

def why_ocazion(request):
	return render(request,"why-ocazion.html")


def display(request):
	queryset_list = Venue.objects.all()
	query = request.GET.get("q")
	f = VenueFilter(request.GET, queryset=Venue.objects.all())
	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(address__icontains=query)|
				Q(area__icontains=query)|
				Q(price__icontains=query)
				).distinct()


	paginator = Paginator(queryset_list, 9)
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"filter" : f,
	}
	return render(request, "index.html", context)

def show(request, id=None):
	instance = get_object_or_404(Venue, id=id)
	form = ReviewForm(request.POST or None, request.FILES or None)
	user = User.objects.filter(name = request.user)
	if user:
		if(Venue.objects.get(id=id) not in user.interested.all()):
			user.interested.add(Venue.objects.get(id=id))
		else:
			user.intersted.remove(Venue.objects.get(id=id))
	if form.is_valid():
		review_instance = form.save(commit=False)
		review_instance.user = user
		review_instance.venue__id = instance.id
		review_instance.save()
		messages.success(request, "Successfully Created")
	reviews = Reviews.objects.filter(venue__id = instance.id)
	if 1:
		context = {
			"instance" : instance,
			"title" : instance.name,
			"reviews" : reviews,
			"form" : form,
		}
		return render(request, "detail.html", context)
	else:
		return HttpResponseNotFound('<h1>Page not found</h1>')
