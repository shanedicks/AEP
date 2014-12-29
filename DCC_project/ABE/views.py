from django.shortcuts import get_object_or_404, render 
from django.http import HttpResponse
from django.views import generic

from ABE.models import Course, Student, Teacher, Skill 

# Create your views here.
def home(request):
	return render(request, 'ABE/home.html')

def schedule(request):
	return render(request, 'ABE/schedule.html')

def calendar(request):
	return render(request, 'ABE/calendar.html')

class CourseList(generic.ListView):
	template_name = 'ABE/course_list.html'
	model = Course

class StudentList(generic.ListView):
	template_name = 'ABE/student_list.html'
	model = Student

class StudentDetail(generic.DetailView):
	template_name = 'ABE/student_profile.html'
	model = Student	

class TeacherList(generic.ListView):
	template_name = 'ABE/teacher_list.html'
	model = Teacher

class TeacherDetail(generic.DetailView):
	template_name = 'ABE/teacher_profile.html'
	model = Teacher	

class SkillList(generic.ListView):
	template_name = 'ABE/skill_list.html'
	model = Skill

def profile(request):
	return HttpResponse('This is a temporary placeholder')

