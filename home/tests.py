from django.test import TestCase, Client, override_settings, RequestFactory
from django.contrib.auth.models import User
from django.db import models

from django.contrib.staticfiles import finders
from home.models import UserProfile

from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

# test case to check if home page is loaded
# before running, do `python manage.py collectstatic`


class LoginTestCase(TestCase):
    def setUp(self):
        # setting up user
        settings_manager = override_settings(SECURE_SSL_REDIRECT=False)
        settings_manager.enable()
        self.addCleanup(settings_manager.disable)

        self.user = User.objects.create_user(
            username='tester')
        self.user.set_password('12345')
        self.user.save()

        self.client = Client()

    # checks to see if login page is loaded

    def test_load_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
    # check to see if home page redirects

    def test_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 301)

    def test_notloggedin_home_page(self):
        login = self.client.login(username='tester', password='12345')
        response = self.client.get('/home')
        self.assertTrue(response.status_code, 200)

    # checks to see if logged in when on map page

    def test_login_mappage(self):
        login = self.client.login(username='tester', password='12345')

        response = self.client.get('/map')
        self.assertTrue(response.status_code, 200)

    # check redirect if logged in but go to login page
    def test_loggedin_login(self):
        login = self.client.login(username='tester', password='12345')
        response = self.client.get('/')
        self.assertTrue(response.status_code, 302)

    # check redirect if not logged in and trying to view map
    def test_notloggedin_map(self):
        response = self.client.get('/map')
        # 301 URL redirect
        self.assertEqual(response.status_code, 301)

    # check users_list view

    def test_user_list_notloggedin(self):
        response = self.client.get('/users_list')
        self.assertEqual(response.status_code, 301)

    def test_user_list_loggedin(self):
        login = self.client.login(username='tester', password='12345')
        response = self.client.get('/users_list')
        self.assertTrue(response.status_code, 301)

    # should redirect bc you can't get to logout page without first logging in

    # check logged out view
    def test_notloggedin_logout(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 301)

    def test_loggedin_logout(self):
        login = self.client.login(username='tester', password='12345')
        response = self.client.get('/logout')
        self.assertTrue(response.status_code, 200)

    # check updateprofileout view
    def test_notloggedin_editprofile(self):
        response = self.client.get('/updateprofile')
        self.assertEqual(response.status_code, 301)

    def test_loggedin_editprofile(self):
        login = self.client.login(username='tester', password='12345')
        response = self.client.get('/updateprofile')
        self.assertTrue(response.status_code, 200)

    def testCSS(self):
        # Get store page
        response = finders.find("style.css")
        # Check it's 200
        self.assertIn("style.css", response)
        self.assertNotEqual(response, None)

# test the user profile


class UserProfileTestCase(TestCase):
    def setUp(self):
        # setting up user
        settings_manager = override_settings(SECURE_SSL_REDIRECT=False)
        settings_manager.enable()
        self.addCleanup(settings_manager.disable)

        self.user = User.objects.create_user(
            username='tester')
        self.user.set_password('12345')
        self.user.first_name = 'Kid'
        self.user.last_name = 'Last'
        self.user.save()

        self.client = Client()


    def test_username(self):
        self.assertEqual(self.user.username, 'tester')

    def test_changeusername(self):
        self.user.username = 'BlueberryPie'
        self.user.save()

        self.assertEqual(self.user.username, 'BlueberryPie')

    def test_online(self):
        self.assertFalse(self.user.userprofile.online, False)

    def test_online_non_uva_email(self):
        login = self.client.login(username='tester', password='12345')
        response = self.client.get('/map')
        self.assertFalse(self.user.userprofile.online, False)

    def test_longitude(self):
        self.assertEqual(self.user.userprofile.longitude, 0.0000000)

    def test_changed_longitude(self):
        self.user.userprofile.longitude = 0.0000001
        self.user.userprofile.save()

        self.assertEqual(self.user.userprofile.longitude, 0.0000001)

    def test_first_name(self):
        self.assertEqual(self.user.first_name, 'Kid')

    def test_changedfirst_name(self):
        self.user.first_name = 'Student'
        self.user.save()

        self.assertEqual(self.user.first_name, 'Student')

    def test_last_name(self):
        self.assertEqual(self.user.last_name, 'Last')

    def test_changedlast_name(self):
        self.user.last_name = 'Teacher'
        self.user.save()

        self.assertEqual(self.user.last_name, 'Teacher')

    def test_change_email(self):
        self.user.email = '1234@gmail.com'
        self.user.save()

        self.assertEqual(self.user.email, '1234@gmail.com')

    def test_latitude(self):
        self.assertEqual(self.user.userprofile.latitude, 0.0000000)

    def test_changed_latitude(self):
        self.user.userprofile.latitude = 0.0000001
        self.user.userprofile.save()

        self.assertEqual(self.user.userprofile.latitude, 0.0000001)

    def test_status(self):
        self.assertEqual(self.user.userprofile.status, 'Hanging Out')

    def test_changed_status(self):
        self.user.userprofile.status = "Changed It!"
        self.user.userprofile.save()

        self.assertEqual(self.user.userprofile.status, 'Changed It!')

    def test_subject(self):
        self.assertEqual(self.user.userprofile.subject, 'School Work')

    def test_changed_subject(self):
        self.user.userprofile.subject = "Changed It!"
        self.user.userprofile.save()

        self.assertEqual(self.user.userprofile.subject, 'Changed It!')
