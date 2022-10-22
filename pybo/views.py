from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Question

def index(request): # request: django에 의해 자동으로 전달되는 HTTP 요청 객체
    """
    목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context) # 페이지 요청에 대한 응답
    # render 함수는 context에 있는 Question 모델 데이터 question_list를 HTML에 적용

def detail(request, question_id):
    """
    내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)