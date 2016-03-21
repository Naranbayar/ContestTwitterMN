from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'home.views.home'),
    url(r'^add$', 'home.views.add'),
    url(r'^map$', 'home.views.map'),
    url(r'^page$', 'home.views.page'),
    url(r'^add_contest$', 'home.views.add_contest'),
    url(r'^tweetEvening$', 'home.views.tweetEvening'),
    url(r'^tweetMorning$', 'home.views.tweetMorning'),
    url(r'^tweetAlways$', 'home.views.tweetAlways'),
)
