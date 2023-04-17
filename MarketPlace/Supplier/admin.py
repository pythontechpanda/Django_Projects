from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Qualification)
admin.site.register(LookingFor)
admin.site.register(CoursesOptions)
admin.site.register(CompanyProfile)
admin.site.register(CreatePost)
admin.site.register(LikePost)
admin.site.register(CommentForPost)
admin.site.register(InsightfulPost)