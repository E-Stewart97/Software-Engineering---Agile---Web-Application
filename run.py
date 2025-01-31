from app import create_app, db
from flask_migrate import Migrate
# from flask_script import Manager
# from flask_migrate import MigrateCommand

app = create_app()
migrate = Migrate(app, db)
# manager = Manager(app)

# manager.add_command('db', MigrateCommand)
# with app.app_context(): # Create app context
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()