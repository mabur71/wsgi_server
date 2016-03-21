from django.conf.urls import patterns, include, url



from django.contrib import admin

admin.autodiscover()



from qa.views import main_page

from qa.views import popular_page

from qa.views import question_id_page 

from qa.views import add_ask_page 

from qa.views import add_answer 

from qa.views import signup_page 

from qa.views import login_page 

from qa.views import logout_page 



urlpatterns = patterns('',

    # Examples:

    # url(r'^$', 'ask.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),



    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', main_page, name='main_page'),

    url(r'^popular/$', popular_page, name='popular_page'),

    url(r'^question/(?P<question_id>(\d)+)/$', question_id_page, name='question_id_page' ),

    url(r'^ask/', add_ask_page, name = 'add_ask_page'),

    url(r'^answer/', add_answer, name='add_answer'),

    url(r'^signup/', signup_page, name='signup_page'),

    url(r'^login/', login_page, name='login_page'),

    url(r'^logout/', logout_page, name='logout_page'),

    #url(r'^new/', include('qa.urls')),

    #url(r'^', include('qa.urls')),

)
