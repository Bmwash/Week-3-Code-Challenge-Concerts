This application Concert domain uses SQLAlchemy with three models: Band, Venue, and Concert.
     > Band has many Concerts.
     > Venue has many Concerts.
     > Concert belongs to both a Band and a Venue.
     > Band and Venue have a many-to-many relationship through Concert.
The application structure looks as below:
       models.py: Contains SQLAlchemy models for Band, Venue, and Concert.
       migrations/: Contains migration scripts and Alembic configuration.
       env.py: Configures Alembic to use SQLAlchemy models for migrations.
Setup procedure
      install dependancies using pipenv install and pipenv shell
      create sqlite3 db and create bands and venues tables
      create models.py file that will contain sqlarchamy models for band,venue & concert
      configure database url to connect to sqlite3 database
      create and initiatlize migration run (alembic init migrations)
      create migration scripts by running (alembic revision --autogenerate -m "Initial migration for bands, venues, and concerts")
      Then create the database by running (alembic upgrade head) and apply the migrations

