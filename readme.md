<p>Run</p>
<p>pipenv shell</p>
<p>python manage.py migrate</p>
<p>python manage.py runserver</p>
<p>python manage.py createsuperuser</p>



# Run with docker-compose
<p>1. Build containers and run them</p>
<p>docker-compose build</p>
<p>docker-compose up -d</p>
<p>2. Create super user</p>
<p>docker exec -it blog_web_1 python manage.py createsuperuser</p>