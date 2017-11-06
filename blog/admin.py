from django.contrib import admin
from .models import Post,Answer,cal4_ans

admin.site.register(Post)

class AnswerAdmin(admin.ModelAdmin):
	list_display=('name','sn','mobile','email','phone','password')

admin.site.register(Answer,AnswerAdmin)
admin.site.register(cal4_ans)
