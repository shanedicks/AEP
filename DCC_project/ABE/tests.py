from django.test import TestCase, LiveServerTestCase, Client
import datetime
from ABE.models import Session

# Create your tests here.

class SessionTest(TestCase):
	def test_create_session(self):
		#create the session
		session = Session()

		#set attributes
		session.start_date = datetime.date(2014, 9, 3)
		session.end_date = datetime.date(2014, 10, 31)

		#saving
		session.save()

		#can we find it
		all_sessions = Session.objects.all()
		self.assertEquals(len(all_sessions), 1)
		only_session = all_sessions[0]
		self.assertEquals(only_session, session)

		#check attributes
		self.assertEquals(only_session.start_date, session.start_date)
		self.assertEquals(only_session.end_date, session.end_date)

class AdminTest(LiveServerTestCase):
	def test_login(self):
		c = Client()

		response = c.get('/admin/')

		self.assertEquals(response.status_code, 200)

		self.assertTrue('Log in' in response.content)
		