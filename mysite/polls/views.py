
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , Http404  
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        }

    # return render(request, 'polls/index.html', context)

    return HttpResponse(template.render(context, request))

    # title = '<h2>Listando as últimas mensagens</h2><hr>'
    # # output = ', '.join([q. question_text for q in latest_question_list])
    # output = '<h4>'
    # for q in latest_question_list:
    #     output += f'    <li> ... id:({q.id}) ...<i> {q.question_text}</i></li>'
    # output = title + output + '</h4>'
    # return HttpResponse(output)

    # return HttpResponse("<h2>Hello, world!!<br><br> You're at the pools index.</h2><hr>")


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse(f"<h2>You're looking at question: ... {question_id} ...</h2><hr>")


def results(request, question_id):
    return HttpResponse(f"<h2>You're looking at the results of question: ... {question_id} ...</h2><hr>")


def vote(request, question_id):
    return HttpResponse(f"<h2>You're voting on question: ... {question_id} ...</h2><hr>")


def info(request):
    return HttpResponse("<h2><u>Framework Django 3.0</u> </h2><hr><h4><ol><li>Rodando no WampServer 3.2.3 </li>   <li> Agora BD MySQL 8.0.1 </li></ol></h4>")

