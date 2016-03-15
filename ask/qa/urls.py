from django.conf.urls import patterns, url

from qa.views import test

urlpatterns = patterns('qa.views',
    #url(r'^$', main_page, name='main_page'),
    #url(r'^(?P<question_id>\d+)/$', views.test, name='question_id'),
    url(r'^', test, name='index'),
)

