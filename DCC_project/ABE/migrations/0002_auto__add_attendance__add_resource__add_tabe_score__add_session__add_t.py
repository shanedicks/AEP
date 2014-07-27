# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attendance'
        db.create_table(u'ABE_attendance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Session'])),
            ('student_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Student'])),
            ('course_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Course'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time_in', self.gf('django.db.models.fields.TimeField')()),
            ('time_out', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'ABE', ['Attendance'])

        # Adding model 'Resource'
        db.create_table(u'ABE_resource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('resource_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('resource_link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('resource_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'ABE', ['Resource'])

        # Adding model 'TABE_Score'
        db.create_table(u'ABE_tabe_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Session'])),
            ('reading_test', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('math_test', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('language_test', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('reading_ge', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('math_comp_ge', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('applied_math_ge', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('language_ge', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
        ))
        db.send_create_signal(u'ABE', ['TABE_Score'])

        # Adding model 'Session'
        db.create_table(u'ABE_session', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ABE', ['Session'])

        # Adding model 'Teacher'
        db.create_table(u'ABE_teacher', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'ABE', ['Teacher'])

        # Adding M2M table for field courses on 'Teacher'
        m2m_table_name = db.shorten_name(u'ABE_teacher_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('teacher', models.ForeignKey(orm[u'ABE.teacher'], null=False)),
            ('course', models.ForeignKey(orm[u'ABE.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['teacher_id', 'course_id'])

        # Adding model 'Course'
        db.create_table(u'ABE_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Session'])),
        ))
        db.send_create_signal(u'ABE', ['Course'])

        # Adding M2M table for field covered_skills on 'Course'
        m2m_table_name = db.shorten_name(u'ABE_course_covered_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'ABE.course'], null=False)),
            ('skill', models.ForeignKey(orm[u'ABE.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'skill_id'])

        # Adding model 'HiSET_Practice_Score'
        db.create_table(u'ABE_hiset_practice_score', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Session'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('math', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('science', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('social_studies', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('reading', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('writing', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
            ('essay', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=0)),
        ))
        db.send_create_signal(u'ABE', ['HiSET_Practice_Score'])

        # Adding model 'Pathway'
        db.create_table(u'ABE_pathway', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'ABE', ['Pathway'])

        # Adding M2M table for field skills on 'Pathway'
        m2m_table_name = db.shorten_name(u'ABE_pathway_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pathway', models.ForeignKey(orm[u'ABE.pathway'], null=False)),
            ('skill', models.ForeignKey(orm[u'ABE.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pathway_id', 'skill_id'])

        # Adding model 'Skill'
        db.create_table(u'ABE_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ABE', ['Skill'])

        # Adding M2M table for field resources on 'Skill'
        m2m_table_name = db.shorten_name(u'ABE_skill_resources')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('skill', models.ForeignKey(orm[u'ABE.skill'], null=False)),
            ('resource', models.ForeignKey(orm[u'ABE.resource'], null=False))
        ))
        db.create_unique(m2m_table_name, ['skill_id', 'resource_id'])

        # Adding model 'Availability'
        db.create_table(u'ABE_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('last_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('day_of_week', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('start_busy_time', self.gf('django.db.models.fields.TimeField')()),
            ('stop_busy_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'ABE', ['Availability'])

        # Adding model 'Student'
        db.create_table(u'ABE_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('pathway_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ABE.Pathway'])),
        ))
        db.send_create_signal(u'ABE', ['Student'])

        # Adding M2M table for field courses on 'Student'
        m2m_table_name = db.shorten_name(u'ABE_student_courses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'ABE.student'], null=False)),
            ('course', models.ForeignKey(orm[u'ABE.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'course_id'])

        # Adding M2M table for field mastered_skills on 'Student'
        m2m_table_name = db.shorten_name(u'ABE_student_mastered_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'ABE.student'], null=False)),
            ('skill', models.ForeignKey(orm[u'ABE.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'skill_id'])

        # Adding M2M table for field in_progress_skills on 'Student'
        m2m_table_name = db.shorten_name(u'ABE_student_in_progress_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'ABE.student'], null=False)),
            ('skill', models.ForeignKey(orm[u'ABE.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'skill_id'])

        # Adding M2M table for field targeted_skills on 'Student'
        m2m_table_name = db.shorten_name(u'ABE_student_targeted_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'ABE.student'], null=False)),
            ('skill', models.ForeignKey(orm[u'ABE.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['student_id', 'skill_id'])


    def backwards(self, orm):
        # Deleting model 'Attendance'
        db.delete_table(u'ABE_attendance')

        # Deleting model 'Resource'
        db.delete_table(u'ABE_resource')

        # Deleting model 'TABE_Score'
        db.delete_table(u'ABE_tabe_score')

        # Deleting model 'Session'
        db.delete_table(u'ABE_session')

        # Deleting model 'Teacher'
        db.delete_table(u'ABE_teacher')

        # Removing M2M table for field courses on 'Teacher'
        db.delete_table(db.shorten_name(u'ABE_teacher_courses'))

        # Deleting model 'Course'
        db.delete_table(u'ABE_course')

        # Removing M2M table for field covered_skills on 'Course'
        db.delete_table(db.shorten_name(u'ABE_course_covered_skills'))

        # Deleting model 'HiSET_Practice_Score'
        db.delete_table(u'ABE_hiset_practice_score')

        # Deleting model 'Pathway'
        db.delete_table(u'ABE_pathway')

        # Removing M2M table for field skills on 'Pathway'
        db.delete_table(db.shorten_name(u'ABE_pathway_skills'))

        # Deleting model 'Skill'
        db.delete_table(u'ABE_skill')

        # Removing M2M table for field resources on 'Skill'
        db.delete_table(db.shorten_name(u'ABE_skill_resources'))

        # Deleting model 'Availability'
        db.delete_table(u'ABE_availability')

        # Deleting model 'Student'
        db.delete_table(u'ABE_student')

        # Removing M2M table for field courses on 'Student'
        db.delete_table(db.shorten_name(u'ABE_student_courses'))

        # Removing M2M table for field mastered_skills on 'Student'
        db.delete_table(db.shorten_name(u'ABE_student_mastered_skills'))

        # Removing M2M table for field in_progress_skills on 'Student'
        db.delete_table(db.shorten_name(u'ABE_student_in_progress_skills'))

        # Removing M2M table for field targeted_skills on 'Student'
        db.delete_table(db.shorten_name(u'ABE_student_targeted_skills'))


    models = {
        u'ABE.attendance': {
            'Meta': {'object_name': 'Attendance'},
            'course_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Course']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Session']"}),
            'student_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Student']"}),
            'time_in': ('django.db.models.fields.TimeField', [], {}),
            'time_out': ('django.db.models.fields.TimeField', [], {})
        },
        u'ABE.availability': {
            'Meta': {'object_name': 'Availability'},
            'day_of_week': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'start_busy_time': ('django.db.models.fields.TimeField', [], {}),
            'stop_busy_time': ('django.db.models.fields.TimeField', [], {}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ABE.course': {
            'Meta': {'object_name': 'Course'},
            'covered_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ABE.Skill']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Session']"}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ABE.hiset_practice_score': {
            'Meta': {'object_name': 'HiSET_Practice_Score'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'essay': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'math': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'reading': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'science': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Session']"}),
            'social_studies': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'writing': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '0'})
        },
        u'ABE.pathway': {
            'Meta': {'object_name': 'Pathway'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ABE.Skill']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ABE.resource': {
            'Meta': {'object_name': 'Resource'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resource_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'resource_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'resource_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ABE.session': {
            'Meta': {'object_name': 'Session'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'ABE.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resources': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ABE.Resource']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ABE.student': {
            'Meta': {'object_name': 'Student'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ABE.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress_skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'in progress+'", 'symmetrical': 'False', 'to': u"orm['ABE.Skill']"}),
            'mastered_skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'mastered+'", 'symmetrical': 'False', 'to': u"orm['ABE.Skill']"}),
            'pathway_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Pathway']"}),
            'targeted_skills': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'targeted+'", 'symmetrical': 'False', 'to': u"orm['ABE.Skill']"}),
            'user_id': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'ABE.tabe_score': {
            'Meta': {'object_name': 'TABE_Score'},
            'applied_math_ge': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_ge': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'language_test': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'math_comp_ge': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'math_test': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'reading_ge': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'reading_test': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ABE.Session']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ABE.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'courses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ABE.Course']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ABE']