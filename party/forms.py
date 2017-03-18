from .models import Venue, Reviews
import django_filters
from django import forms

class VenueFilter(django_filters.FilterSet):
	#https://django-filter.readthedocs.org/en/latest/ref/filters.html
	min_range = django_filters.NumberFilter(name='max_price', lookup_expr='gte')
	max_range = django_filters.NumberFilter(name='min_price', lookup_expr='lte')
	address = django_filters.CharFilter(name = 'address', lookup_expr='icontains')
	zone = django_filters.CharFilter(name= 'zone', lookup_expr='iexact')
	class Meta:
		model = Venue
		fields = {
			'max_range',
			'min_range',
			'address',
			'zone',
		}

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Reviews
		fields = {
			'description',
		}
	def __init__(self, *args, **kwargs):
		super(ReviewForm, self).__init__(*args, **kwargs)
		self.fields['description'].label = "Give Review"