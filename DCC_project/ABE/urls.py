from django.conf.urls import patterns, url
from ABE.views import CourseList, StudentList, TeacherList, SkillList

urlpatterns = patterns('ABE.views',
	url(r'^$', 'home'),
	url(r'^schedule/$', 'schedule'),
    url(r'^calendar/$', 'calendar'),
    url(r'^profile/$', 'profile'),
)

urlpatterns += patterns('',
    url(r'^courses/$', CourseList.as_view()),
    url(r'^students/$', StudentList.as_view()),
    url(r'^teachers/$', TeacherList.as_view()),
    url(r'^skills/$', SkillList.as_view()),
)