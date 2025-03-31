## DAY CARE CENTER

* Having the possibility to erase data of an outgoing student, while creating new data for the incoming ones,
will make my job alot smoother, as a staff.

* Adding parents profile to their child/ward data will make contacting them in times of an emergency alot easier.

* As staffs it will make our job go alot smoother if we can have an inbox for the user experience were their
messages are stored for queries and inquiry purposes.

* As tutors having a place were we can store the pupils projects for viewing, so parents can be updated on their ward's latest school projects and can browse in easily, will come in really handy.

* As a new parent enrolling their ward i would love to be able to register in my details and that of my child only once so i can easily longin and out without having to update my info everytime i'm loggedin.

* As parents forgetting passwords are common with us i will like a user experience that allows me change or retrive a lost password easily by just updating my email addressing.

* As a staff i would like the student to have a registration number, this will make differntiating students with
similar data alot easier.

# models/model

# * Students: string
# * Students registration number: foreign key - autoincrementing integer
# * Fess: decimal
# * Staff: string
# * Email: string
# * Staff: primary key
# * Parent/user: string
# * Time/hours: integer

# APPS

* projects
* Users
* Staffs 
* inbox

link to database: postgresql://projects_db_putp_user:7hxuYhca8G7XOKtnCXZQoFFMGXdNEb7p@dpg-cvfantl2ng1s73d450ng-a.frankfurt-postgres.render.com/projects_db_putp

github repo https://github.com/annunquee/django_daycare.git

admin user on the local server is (admin) with password (admin)

render.com https://django-daycare.onrender.com
here: users name (Admin)and password is (admin) https://django-daycare.onrender.com/admin/

you can also enter this in shell, after running python manage.py shell       
print(CustomUser.objects.filter(is_superuser=True).values('username', 'is_staff', 'is_superuser'))
to confirm superuser.

# A few explanation on the fixes

my virtual environment was set to gitignore by accident which broke my code and due to that some installed package on requirement.txt were lost. but not correctly installed as i kept running pip freeze >requirements.txt each time after every pip install, which autamatically saved it properly this time.

i used a defferent aproach this time from the method thought in class for deploying to render. At this stage everything seems perfectly okay after going through your remarks and every single point made was very much considered. 

tasting impplimented much better than before, this time with code in test.py for users, projects and inbox. 

can't chage project name at this point, as this will affect settings.py, wsgi.py and initial render deployment.

more details on logging into render admin is availible on render environment.

i initially left my commented out code to give you an insight on a solution i tried but didn't work before sticking to what i have working.
