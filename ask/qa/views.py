from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question

# Create your views here.
from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('Dummy view.')

def main_page(request):
    posts = Question.objects.filter()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    return render(request, 'main_page.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'title': 'All posts:'
    })

def popular_page(request):
    posts = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page) # Page
    return render(request, 'main_page.html', {
        'posts': page.object_list,
        'paginator': paginator,
        'page': page,
        'title': 'All posts:'
    })
   
    return HttpResponse('Popular question page.')

def question_id_page(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question_post.html', {
        'title': question.title,
        'text': question.text,
        'answers': question.answer_set.all()[:],
    })
