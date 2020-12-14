from django.contrib import admin
from .models import CustomUser

# Register your models here.
# モデルに定義したカスタムユーザーモデルを管理サイトで編集できるようにするための記載。
admin.site.register(CustomUser)