from django.contrib import admin


from .models import Organiser
from .models import Attendee
from .models import Events
from .models import Admin
# Register your models here.
admin.site.register(Organiser)
admin.site.register(Attendee)
admin.site.register(Events)
admin.site.register(Admin)