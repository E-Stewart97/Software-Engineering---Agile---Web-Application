from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import click
from flask.cli import with_appcontext

db = SQLAlchemy() # Create db instance that isn't initialised
migrate = Migrate()

@click.command('seed-db')
@with_appcontext
def seed_db_command():
    """Seed the database."""
    from scripts.seed_data import users_data, customers_data, products_data, customer_products_data
    
    try:
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        # Now seed the data
        db.session.bulk_save_objects(users_data)
        db.session.bulk_save_objects(customers_data)
        db.session.bulk_save_objects(products_data)
        db.session.bulk_save_objects(customer_products_data)
        db.session.commit()
        click.echo('Database seeded successfully!')
    except Exception as e:
        db.session.rollback()
        click.echo(f'Error seeding database: {e}')

def create_app(config_class=Config):
    app = Flask(__name__)  # Create flask app
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import routes  # Import routes after app creation
    app.register_blueprint(routes.bp) # Register routes
    app.cli.add_command(seed_db_command)  # Register the seed-db command
    
    return app