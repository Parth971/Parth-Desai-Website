from django.contrib import admin

from dashboard.models import Skill, Contact

admin.site.register([Skill, Contact])
