from socket import fromshare
from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    """
    장고 폼 (모델 폼)
    """
    class Meta:
        model = Question
        fields = ['subject', 'content']
        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows': 10}),
        }
        수작업으로 HTML을 만들어서 디자인적인것을 넣기 위해선 이렇게 하면 안된다
        """
        labels = {
            'subject': 'Input subject!', # 여기서 label을 입력한거랑 html에서 입력한거랑 적용되는데가 다른가?
            'content': 'Input content!',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'answer'
        }