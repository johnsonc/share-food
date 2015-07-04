1. Create virtualenv

	$cd PROJECT_FOLDER
	$virtualenv ENV_NAME
	$source ENV_NAME/bin/activate

	$pip install -r /webapp/requirements.txt

2. config postgres

	$sudo -i -u postgres
	$<postgres>createdb food
	$<postgres>psql food
	$<postgres><psql>CREATE EXTENSION postgis;

	$<postgres><psql>\q
	$<postgres>exit()
	$
3. change pg_hba.conf:

	$sudo nautilus
	  -- go etc/postgresql/x.y/main/pg_hba.conf
	  -- open pg_hba.conf for edition
          -- change all(or specified one) "peer" and "md5" to "trust"
	  -- save changments
          -- close nautilus
	$ctrl+c

4. syncdb

	$ python manage.py syncdb

	* in case of "preserve_default" error in __init__.py
		pip install django==1.7.1
	   and repeat command

	$ python manage.py create_notices

5. run application
	python manage.py runserver



6. crontab configuration
*/2 * * * * python PATH_TO_THE_APP/manage.py emit_notices
0 9 * * * python PATH_TO_THE_APP/manage.py check_temporal_matches
