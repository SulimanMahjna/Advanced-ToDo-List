from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

user_table = user(

   Column('id', Integer, primary_key=True),
   Column('username', String(100), unique=True),  
   Column('email', String(100), unique=True),     
   Column('user_password', String(100)),          
   Column('created_at', DateTime, default=datetime.utcnow),
   Column('updated_at', DateTime, default=datetime.utcnow)
)




db = SQLAlchemy()

task_status_enum = ENUM(
    'pending', 'in_progress', 'completed', 'cancelled',
    name='task_status',
    create_type=False  
)
tasks_table = Table(
    'tasks', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), nullable=False),
    Column('task_name', Text, nullable=False),
    Column('due_date', DateTime),
    Column('description', Text),
    Column('status', task_status_enum, nullable=False, default='pending'),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime, default=datetime.utcnow)
)
subtask_table = Table(
    'subtask', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('task_id', Integer, ForeignKey('tasks.id'), nullable=False),
    Column('name', Text, nullable=False),
    Column('status', task_status_enum, nullable=False, default='pending'),
    Column('due_date', DateTime),
    Column('description', Text),
    Column('created_at', DateTime, default=datetime.utcnow),
    Column('updated_at', DateTime, default=datetime.utcnow)
)


