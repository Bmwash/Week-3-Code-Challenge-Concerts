This application Concert domain uses SQLAlchemy with three models: Band, Venue, and Concert.
     > Band has many Concerts.
     > Venue has many Concerts.
     > Concert belongs to both a Band and a Venue.
     > Band and Venue have a many-to-many relationship through Concert.
The application structure looks as below:
       models.py: Contains SQLAlchemy models for Band, Venue, and Concert.
       migrations/: Contains migration scripts and Alembic configuration.
       env.py: Configures Alembic to use SQLAlchemy models for migrations.
