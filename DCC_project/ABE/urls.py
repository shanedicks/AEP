from django.conf.urls import patterns, url
from ABE import views

urlpatterns = patterns('ABE.views',
	url(r'^$', 'home'),
	url(r'^schedule/$', 'schedule'),
    url(r'^calendar/$', 'calendar'),
    url(r'^profile/$', 'profile'),
)

urlpatterns += patterns('',
    url(r'^courses/$', views.CourseList.as_view()),
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>\d+)/$', views.StudentDetail.as_view()),
    url(r'^teachers/$', views.TeacherList.as_view()),
    url(r'^teachers/(?P<pk>\d+)/$', views.TeacherDetail.as_view()),    
    url(r'^skills/$', views.SkillList.as_view()),
)