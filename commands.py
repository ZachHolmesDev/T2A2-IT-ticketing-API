from flask import Blueprint
from main import db
from main import bcrypt
from datetime import datetime
from sqlalchemy import text


# models
# from models.categories import Categories 
from models.comment import Comment 
from models.role import Role 
# from models.ticket_categories import TicketCategories
from models.ticket import Ticket
from models.user import User


db_commands = Blueprint("db", __name__)


@db_commands.cli.command('test')
def test_flask():
    print('cli test sucessfull !')


@db_commands.cli.command("drop")
def drop_tables():
    # drop tables
    # Execute a raw SQL query to drop the table using CASCADE
    # db.engine.execute(text("DROP TABLE tickets CASCADE"))
    db.drop_all()
    print("Tables dropped")


@db_commands.cli.command("create")
def create_tables():
    # create tables
    db.create_all()
    print("Tables created")


# seed function is defined seperatly for reuse  
def seed_db_logic():
    print('start seeding')
     # Create roles
    roles = [
        Role(role_name="admin", can_view_all=True, can_manage=True, can_action=True),
        Role(role_name="user", can_view_all=False, can_manage=False, can_action=True),
        Role(role_name="tech", can_view_all=True, can_manage=False, can_action=True)
    ]

    db.session.add_all(roles)
    db.session.commit()

    # Create users
    users = [
        User(
            name          = 'Admin1',
            email         = 'admin@admin.com',
            password_hash = bcrypt.generate_password_hash('admin123').decode('utf-8'),
            role          = roles[0]
        ),
        User(
            name          = 'User Meg2',
            email         = 'user1@email.com',
            password_hash = bcrypt.generate_password_hash('user1pw').decode('utf-8'),
            role          = roles[1]
        ),
        User(
            name          = 'User Bob3',
            email         = 'user2@email.com',
            password_hash = bcrypt.generate_password_hash('user2pw').decode('utf-8'),
            role          = roles[1]
        ),
        User(
            name          = 'User Caleb4',
            email         = 'user3@email.com',
            password_hash = bcrypt.generate_password_hash('user3pw').decode('utf-8'),
            role          = roles[1]
        ),
        User(
            name          = 'Tech Zach5',
            email         = 'tech_Zach@email.com',
            password_hash = bcrypt.generate_password_hash('techpw').decode('utf-8'),
            role          = roles[2]
        ),
        ]

    db.session.add_all(users)
    db.session.commit()

    

    # Create tickets
    tickets = [
        Ticket(
            title      = "Issue 1",   description = "This is issue 1",
            priority   = "High",      status      = "Open",            created_at = datetime.now(),
            created_by_id = users[1].id, assigned_to_id = users[0].id
        ),
        Ticket(
            title      = "Issue 2",   description = "This is issue 2",
            priority   = "Low",       status      = "Closed",          created_at = datetime.now(),
            created_by_id = users[1].id, assigned_to_id = users[4].id
        ),
        Ticket(
            title      = "Issue 3",   description = "This is issue 3",
            priority   = "Medium",    status      = "Open",            created_at = datetime.now(),
            created_by_id = users[2].id, assigned_to_id = users[4].id
        ),
        Ticket(
            title      = "Issue 4",   description = "This is issue 4",
            priority   = "High",      status      = "Closed",          created_at = datetime.now(),
            created_by_id = users[3].id, assigned_to_id = users[4].id
        ),
        Ticket(
            title      = "Issue 5",   description = "This is issue 5",
            priority   = "Low",       status      = "Open",            created_at = datetime.now(),
            created_by_id = users[4].id, assigned_to_id = users[4].id
        ),
        Ticket(
            title      = "Issue 6",   description = "This is issue 6",
            priority   = "Medium",    status      = "Closed",          created_at = datetime.now(),
            created_by_id = users[4].id, assigned_to_id = users[0].id
        ),
            ]
# change to manual assignment of ticket_id cause idk why it wont work like everyone else 
    comments = [
        Comment(content="This is a comment on issue 1 by the user Admin1", 
                created_at=datetime.now(), user_id=users[0].id, ticket_id=1),
        Comment(content="This is a comment on issue 2 by the user Meg2", 
                created_at=datetime.now(), user_id=users[1].id, ticket_id=2),
        Comment(content="This is a comment on issue 3 by the user Bob3", 
                created_at=datetime.now(), user_id=users[2].id, ticket_id=3),
        Comment(content="This is a comment on issue 4 by the user Caleb4", 
                created_at=datetime.now(), user_id=users[3].id, ticket_id=4),
        Comment(content="This is a comment on issue 5 by the user Zach5", 
                created_at=datetime.now(), user_id=users[4].id, ticket_id=5),
        Comment(content="This is a comment on issue 6 by the user Admin1", 
                created_at=datetime.now(), user_id=users[0].id, ticket_id=6,)
        # Comment(content="This is a comment on issue 6 by the user Admin1", 
        #         created_at=datetime.now(), user_id=users[0].id, ticket_id=tickets[5].id),
]

    db.session.add_all(tickets)
    db.session.commit()
    db.session.add_all(comments)
    db.session.commit()

    # # Create categories
    # categories = [
    #     Categories(categorie_name="Hardware Issues"),
    #     Categories(categorie_name="Software Errors"),
    #     Categories(categorie_name="Network Problems"),
    #     Categories(categorie_name="Email and Communication"),
    #     Categories(categorie_name="Security and Access"),
    #     Categories(categorie_name="General Inquiries"),
    # ]

    # db.session.add_all(categories)
    # # db.session.commit()

    # # Link tickets to categories
    # ticket_categories = [
    # TicketCategories(ticket_id=tickets[0].id, category_id=categories[0].id),
    # TicketCategories(ticket_id=tickets[1].id, category_id=categories[1].id),
    # TicketCategories(ticket_id=tickets[2].id, category_id=categories[0].id),
    # TicketCategories(ticket_id=tickets[3].id, category_id=categories[1].id),
    # TicketCategories(ticket_id=tickets[4].id, category_id=categories[0].id),
    # TicketCategories(ticket_id=tickets[5].id, category_id=categories[1].id),
    # ]

    # db.session.add_all(ticket_categories)
    # db.session.commit()

 
    print("Tables seeded")

@db_commands.cli.command("seed")
def seed_db():
    seed_db_logic()

@db_commands.cli.command('reset')
def reset_db_seed():

        
    db.drop_all()
    print("Tables dropped")
    db.create_all()
    print("Tables created")
    seed_db_logic()
    print('Reset Sucess')