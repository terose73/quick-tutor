To run locally, ensure pip/Python3 and Django are correctly installed

1. Run pip install -r requirements.txt in a terminal window
2. Run python manage.py runsslserver in a terminal window

create a .env file with the following variables 

DATABASE_URL=sqlite:///db.sqlite3
GOOGLE_API_KEY={your google api key here w/ google maps enabled}

Application hosted on heroku at   https://segfaults.herokuapp.com/

Once there, you can read the main page for an over view of the project.
In the upper right hand corner you can use your email to sign in.
Once you sign in, please make sure to hit allow for location for the map feature. 
A marker should show up on the map with your location.
Take a look around to see if there are other markers around you, those are also people looking for help or willing to tutor!
Click on a marker to see the user's status, subject focus, and email.
In this way, you can find users nearby, and you can work with them, or contact them for tutoring services!
The possiblities are endless - we've broken the barrier between students and tutors for a collaborative environment. 

You can also check out our user's list which contains all of the users and their status.
Click on their email to send an email to contact them about working with them.
Some may not have an address but that's just because they didn't want it to be shown. 

To update your name, status, or subject focus, head on over to the update profile section.
The button will be in the upper right corner.

Once you're done using the app, please make sure to logout.
The logout button can be found in the upper right corner. 


Framework and Library Licenses:
Django: 3-clause BSD, 
Bootstrap: MIT, 
Django-secure: BSD, 
Gunicorn: MIT, 
Social auth app django: BSD, 
Whitenoise: MIT, 
Django sslserver: BSD, 
PostgresSQL: PostgreSql license, similar to BSD or MIT 

https://github.com/django/django/blob/master/LICENSE
https://getbootstrap.com/docs/4.0/about/license/
https://en.wikipedia.org/wiki/Gunicorn
http://whitenoise.evans.io/en/stable/
https://www.postgresql.org/about/licence/
