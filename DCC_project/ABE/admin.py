from django.contrib import admin
from ABE.models import Session, Skill, Pathway, Course, Teacher, Student, TABE_Score, HiSET_Practice_Score

admin.site.register(Session) 
admin.site.register(Skill)
admin.site.register(Pathway) 
admin.site.register(Course) 
admin.site.register(Teacher) 
admin.site.register(Student) 
admin.site.register(TABE_Score)  
admin.site.register(HiSET_Practice_Score)