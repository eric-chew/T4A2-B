from main import db
from flask import Blueprint

db_commands = Blueprint('db-custom', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created')


@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables deleted')


@db_commands.cli.command('seed')
def seed_db():
    from models.Project import Project
    from models.Feedback import Feedback
    from models.User import User
    from main import bcrypt

    for i in range(4):
        user = User()
        user.username = f'user{i+1}'
        user.email = f'user{i+1}@domain.com'
        user.password = bcrypt.generate_password_hash(
            f'password{i+1}'
        ).decode('utf-8')
        db.session.add(user)

    db.session.commit()

    project1 = Project()
    project1.name = 'Project1'
    project1.link = 'https://google.com/'
    project1.description = 'This is Project 1'
    project1.user_id = 1
    db.session.add(project1)

    project2 = Project()
    project2.name = 'Project2'
    project2.link = 'https://www.youtube.com/'
    project2.description = 'This is Project 2'
    project2.user_id = 1
    db.session.add(project2)

    project3 = Project()
    project3.name = 'Project3'
    project3.link = 'https://www.facebook.com/'
    project3.description = 'This is Project 3'
    project3.user_id = 2
    db.session.add(project3)

    project4 = Project()
    project4.name = 'Project4'
    project4.link = 'https://twitter.com/?lang=en'
    project4.description = 'This is Project 4'
    project4.user_id = 3
    db.session.add(project4)

    db.session.commit()

    feedback1 = Feedback()
    feedback1.text = 'Acceptable'
    feedback1.user_id = 4
    feedback1.project_id = 1
    db.session.add(feedback1)

    feedback2 = Feedback()
    feedback2.text = 'Acceptable'
    feedback2.user_id = 3
    feedback2.project_id = 1
    db.session.add(feedback2)

    feedback3 = Feedback()
    feedback3.text = 'Acceptable'
    feedback3.user_id = 4
    feedback3.project_id = 3
    db.session.add(feedback3)

    feedback4 = Feedback()
    feedback4.text = 'Acceptable'
    feedback4.user_id = 2
    feedback4.project_id = 3
    db.session.add(feedback4)

    feedback5 = Feedback()
    feedback5.text = 'Acceptable'
    feedback5.user_id = 4
    feedback5.project_id = 4
    db.session.add(feedback5)

    db.session.commit()
    print('Tables seeded')
