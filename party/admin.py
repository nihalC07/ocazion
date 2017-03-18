from django.contrib import admin
from .models import User, Venue, Reviews, Pics, Cuisines, Ratings #Memo, Facilities, Suitable, SpaceType
# Register your models here.

admin.site.register(User)
admin.site.register(Venue)
admin.site.register(Reviews)
#admin.site.register(Memo)
admin.site.register(Pics)
admin.site.register(Cuisines)
admin.site.register(Ratings)
#admin.site.register(Facilities)
#admin.site.register(Suitable)
#admin.site.register(SpaceType)

