from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
	title = models.CharField(max_length=20, null=True, blank=True)
	start_date = models.DateField()
	end_date = models.DateField()
	
	def __unicode__(self):
		return self.title

class Resource(models.Model):
	LESSON = 'L'
	ASSESSMENT = 'A'
	RESOURCE = 'R'
	RESOURCE_TYPE_CHOICES = (
		(LESSON,'Lesson Plan'),
		(ASSESSMENT, 'Assessment'),
		(RESOURCE, 'Student Resource'),
	)
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=250)
	resource_file = models.FileField(upload_to = 'files', null=True, blank=True)
	resource_link = models.URLField(null=True, blank=True)
	resource_type = models.CharField(max_length=1, choices=RESOURCE_TYPE_CHOICES)
	
	def __unicode__(self):
		return self.title

class Skill(models.Model):
	title = models.CharField(max_length=20)
	resources = models.ManyToManyField(Resource, null=True, blank=True)
	
	def __unicode__(self):
		return self.title

class Pathway(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=250)
	skills = models.ManyToManyField(Skill,null=True, blank=True)	
	
	def __unicode__(self):
		return self.title

class Course(models.Model):
	JP = 'JP'
	WB = 'WB'
	MC = 'MC'
	CP = 'CP'
	SC= 'SC'
	SITE_CHOICES = (
		(JP, 'Jefferson Parish'),
		(WB, 'West Bank'),
		(MC, 'Mid City'),
		(CP, 'City Park'),
		(SC, 'Sydney Collier'),
	)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	site = models.CharField(max_length=2,
							choices=SITE_CHOICES
							)
	start_time = models.TimeField()
	end_time = models.TimeField()
	covered_skills = models.ManyToManyField(Skill, null=True, blank=True)
	session = models.ForeignKey(Session)			
	
	def __unicode__(self):
		return self.title

class Teacher(models.Model):
	user = models.OneToOneField(User)
	courses = models.ManyToManyField(Course, null=True, blank=True)
	
	def __unicode__(self):
		return unicode(self.user.get_full_name())

class Student(models.Model):
	user = models.OneToOneField(User)
	courses = models.ManyToManyField(Course, null=True, blank=True)
	mastered_skills = models.ManyToManyField(Skill, related_name='mastered+', null=True, blank=True)
	in_progress_skills = models.ManyToManyField(Skill, related_name='in progress+', null=True, blank=True)
	targeted_skills = models.ManyToManyField(Skill, related_name='targeted+', null=True, blank=True)
	pathway_id = models.ForeignKey(Pathway, null=True, blank=True)
	
	def __unicode__(self):
		return unicode(self.user.get_full_name())

class Availability(models.Model):
	MONDAY = 'M'
	TUESDAY = 'T'
	WEDNEDAY = 'W'
	THURSDAY = 'R'
	FRIDAY = 'F'
	SATURDAY = 'S'
	DAY_OF_WEEK_CHOICES = (	
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNEDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
	)
	user = models.ForeignKey(User)
	last_updated = models.DateField(auto_now=True)
	day_of_week = models.CharField(max_length=1, choices=DAY_OF_WEEK_CHOICES)
	start_busy_time = models.TimeField()
	stop_busy_time = models.TimeField()

class Attendance(models.Model):
	session = models.ForeignKey(Session)
	student_id = models.ForeignKey(Student)
	course_id = models.ForeignKey(Course)
	date = models.DateField()
	time_in = models.TimeField()
	time_out = models.TimeField()

class TABE_Score(models.Model):
	A10 = 'a0'
	A9 = 'a9'
	D10 = 'd0'
	D9 = 'd9'
	M10 = 'm0'
	M9 = 'm9'
	E10 = 'e0'
	E9 = 'e9'
	TEST_FORM_CHOICES = (
		(A10, 'A10'),
		(A9, 'A9'),
		(D10, 'D10'),
		(D9, 'D9'),
		(M10, 'M10'),
		(M9, 'M9'),
		(E10, 'E0'),
		(E9, 'E9'),
	)
	user_id = models.ForeignKey(User)
	session = models.ForeignKey(Session)
	reading_test = models.CharField(max_length=2, choices=TEST_FORM_CHOICES)
	math_test = models.CharField(max_length=2, choices=TEST_FORM_CHOICES)
	language_test = models.CharField(max_length=2, choices=TEST_FORM_CHOICES)
	reading_ge = models.DecimalField(max_digits=3, decimal_places=1)
	math_comp_ge = models.DecimalField(max_digits=3, decimal_places=1)
	applied_math_ge = models.DecimalField(max_digits=3, decimal_places=1)
	language_ge = models.DecimalField(max_digits=3, decimal_places=1)	
		
class HiSET_Practice_Score(models.Model):
	LONG = 'l'
	SHORT = 's'
	FORM_CHOICES = (
		(LONG, 'Long Form'),
		(SHORT, 'Short Form'),
	)
	user_id = models.ForeignKey(User)
	session = models.ForeignKey(Session)
	date = models.DateField()
	math = models.DecimalField(max_digits=2, decimal_places=0)
	science = models.DecimalField(max_digits=2, decimal_places=0)
	social_studies = models.DecimalField(max_digits=2, decimal_places=0)
	reading = models.DecimalField(max_digits=2, decimal_places=0)
	writing = models.DecimalField(max_digits=2, decimal_places=0)
	essay = models.DecimalField(max_digits=2, decimal_places=0)
	
	
			
	

