from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Chanel)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(UserLiked)
admin.site.register(Subscriber)
admin.site.register(UserRoot)