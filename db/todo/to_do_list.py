"""To Do List Programe"""
"""Represent a Tasks in the To-DoList. 
match against a string in searches and store each tasks"""

import datetime
import sqlite3

db = 'todo.db'

class Task:
    def __init__(self, details, deadline, status = 0, project='pycat'):
        self.details = details
        self.status = status
        self.deadline = deadline
        self.project = project
        self.priority = 1
        self.completed_on = ''
    
    # details, status, deadline, project
    # id           integer primary key autoincrement not null,
    # priority     integer default 1,
    # details      text,
    # status       text,
    # deadline     date,
    # completed_on date,
    # project      text not null references project(name)

class ToDoList:
    """Represent a collection of tasks that 
    can be searched, modified and complete and deleted """

    def __init__(self):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("""select id, priority, details, status, deadline from task where project = 'pycat' order by deadline""")
            self.tasks = cursor.fetchall()

    def all_tasks(self):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute("""select id, priority, details, status, deadline from task where project = 'pycat' order by deadline""")
            return cursor.fetchall()

    def new_task(self, details, deadline):
        """Create new task and add it to the list"""
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            query = "insert into task (details, deadline, project) values(?, ?, ?)"
            cursor.execute(query, (details, deadline, 'pycat'))
            # Commit your changes in the database
            conn.commit()

    def update_task(self, id, status):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            query = "update task set status = :status where id = :id"
            cursor.execute(query, {'status': status, 'id': id})
            conn.commit()

    def delete_task(self, id):
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM task WHERE id = :id"
            cursor.execute(query, {'id': id})
            conn.commit()
        
    def search(self, q):
        """Find all task that match the given 
        fliter string """
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            query = "select * from task WHERE details LIKE ?"
            cursor.execute(query, (f'%{q}%',))
            return cursor.fetchall()