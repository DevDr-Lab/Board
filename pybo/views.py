from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse
from .models import Answer, Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator # 페이징 기능 추가 위한 모듈

def index(request): # request: django에 의해 자동으로 전달되는 HTTP 요청 객체
    """
    목록 출력
    """
    # 입력
    page = request.GET.get('page', '1')
    
    #조회
    question_list = Question.objects.order_by('-create_date')
    
    # 페이징 처리
    paginator = Paginator(question_list, 10) # 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context) # 페이지 요청에 대한 응답
    # render 함수는 context에 있는 Question 모델 데이터 question_list를 HTML에 적용

def detail(request, question_id):
    """
    내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # answer model을 사용해서 데이터를 저장할 수도 있다

    return 

def question_create(request):
    """
    질문 등록
    """
    if request.method == "POST": # POST라면 화면에서 전달받은 데이터로 폼의 값이 채워지도록 객체를 생성
        form = QuestionForm(request.POST)
        if form.is_valid(): # 요청받은 form이 유효한지 검사
            question = form.save(commit=False) # form으로 Question 모델 데이터를 저장하기 위한 코드, commit=False는 임시저장을 의미, 아래에서 date를 받고난 뒤에 저장하도록 하기 위해?
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else: # GET 방식이라면 입력값 없이 객체를 생성
        form = QuestionForm()
    context = {'form': form} # {'form': form}은 폼엘리먼트를 생성할 때 사용
    return render(request, 'pybo/question_form.html', context) 
