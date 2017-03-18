from __future__ import unicode_literals

from django.db import models

from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse

class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name):
        return name

def upload_location_main(instance, filename):
	return "%s/%s" %(instance.name+str(instance.phone), str(instance.phone))

def upload_location_other(instance, filename):
	return "%s/%s/%s" %(instance.venue.id, instance.venue.name, filename)

class Cuisines(models.Model):
	name = models.CharField(max_length = 30, primary_key = True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name


class User(models.Model):
	name = models.CharField(max_length = 30, null = False, blank = False)
	email = models.EmailField(max_length = 50)
	phone = models.IntegerField(null = False, blank = False)
	code = models.IntegerField(blank = False)
	landline = models.IntegerField(blank = False)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name


class Venue(models.Model):
	name = models.CharField(max_length = 30, null = False, blank = False)
	address = models.CharField(max_length = 70, null = False, blank = False)
	capacity = models.IntegerField()
	associated = models.BooleanField(default = True)
	contact_person = models.CharField(max_length = 30)
	phone = models.BigIntegerField(null = False, blank = False)
	std_code = models.IntegerField(blank = False)
	landline = models.IntegerField(blank = False)
	area = models.CharField(max_length = 20)
	min_price = models.IntegerField(null = False, blank = False)
	max_price = models.IntegerField(null = False, blank = False)
	zone = models.CharField(max_length = 30)
	cuisines = models.ManyToManyField(Cuisines)
	outside_catering = models.BooleanField(default = False)
	decor = models.BooleanField(default = False)
	no_of_venues = models.IntegerField()
	non_veg = models.BooleanField(default = True)
	extra_details = models.TextField(max_length = 500)
	car_parking = models.IntegerField()
	description = models.TextField(max_length = 1000)
	map_link = models.CharField(max_length = 3000)
	pic = models.ImageField(upload_to = upload_location_main)
	rated_by = models.BigIntegerField(default=0)
	avg_rating = models.FloatField(default=3)
	rated_user = models.ManyToManyField(User, blank=True)

	#def ratings(self, rating):
	#	self.avg_rating = (self.avg_rating * self.rated_by + rating) / (self.rated_by + 1)
	#	self.rated_by += 1

	#def get_absolute_url(self):
	#	name = self.name.replace(' ','-')
	#	return "/"+str(self.id)+"/"+name

	def get_absolute_url(self):
		return reverse("show", kwargs={"id":self.id})	

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name


class Ratings(models.Model):
	rating = models.IntegerField()
	user = models.ForeignKey(User)
	venue = models.ForeignKey(Venue)

	def __str__(self):
		return self.venue.name

	def __unicode__(self):
		return self.venue.name


class Reviews(models.Model):
	user = models.ForeignKey(User)
	description = models.TextField(max_length = 200)
	timestamp = models.DateTimeField(auto_now = True)
	venue = models.ForeignKey(Venue)

	def __str__(self):
		return self.venue.name

	def __unicode__(self):
		return self.venue.name


class Pics(models.Model):
	venue = models.ForeignKey(Venue)
	image = models.ImageField(upload_to = upload_location_other) # need to set upload_to 

	def __str__(self):
		return self.venue.name

	def __unicode__(self):
		return self.venue.name






#def upload_location_memo(instance, filename):
#	return "memo/%s/%s/%s" %(instance.venue.name, instance.user.name, instance.id)
#
#class Facilities(models.Model):
#	name = models.CharField(max_length = 30, primary_key = True)
#
#	def __str__(self):
#		return self.name
#
#	def __unicode__(self):
#		return self.name
#
#
#class Suitable(models.Model):
#	name = models.CharField(max_length = 30, primary_key = True)
#
#	def __str__(self):
#		return self.name
#
#	def __unicode__(self):
#		return self.name
#
#
#class SpaceType(models.Model):
#	name = models.CharField(max_length = 30, primary_key = True)
#
#	def __str__(self):
#		return self.name
#
#	def __unicode__(self):
#		return self.name
#
#
#class Memo(models.Model):
#	image = models.ImageField(upload_to = upload_location_memo)
#	user = models.ForeignKey('User')
#	venue = models.ForeignKey('Venue')
#
#	def __str__(self):
#		return self.venue.name
#
#	def __unicode__(self):
#		return self.venue.name


