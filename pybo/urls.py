from django.urls import path
from . import views

# urls.py는 페이지 요청 시 가장 먼저 호출되며 요청 url과 뷰 함수를 1:1로 연결해준다

app_name = 'pybo' # namespace 사용함

urlpatterns =[
    path('', views.index, name='index'), # views.index: views.py파일의 index함수를 의미한다
    # config/urls.py에서 pybo/에 대한 처리를 했으므로 ''를 넘겨주어야 한다
    # 맨 뒤에 항상 쉼표를 달자
    path('<int:question_id>/', views.detail, name='detail'), # URL매핑에 name 속성을 부여한다
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'), # url 마지막에는 / 붙이는걸 습관화 하자
]