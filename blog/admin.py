from django.contrib import admin
from .models import Post,Answer

admin.site.register(Post)

class AnswerAdmin(admin.ModelAdmin):
	list_display=('name','sn','mobile','email','phone','password')

admin.site.register(Answer,AnswerAdmin)