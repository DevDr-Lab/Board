from django.contrib import admin

# Register your models here.

# 만든 모델을 여기에 등록하면 모델을 관리하기 쉽다
# 장고 셸로 수행한 데이터 저장, 수정, 삭제 등의 작업을 admin에서 할 수 있다.

from .models import Question



class QuestionAdmin(admin.ModelAdmin): # 검색필드 추가
    search_fields =  ['subject']

admin.site.register(Question, QuestionAdmin)