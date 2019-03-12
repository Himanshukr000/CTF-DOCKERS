#!/usr/bin/env python3

"""dbinit.py -- imports tasks and init database"""

import dataset
import json
import sys
import time

if __name__ == '__main__':

    # Load the json structure
    tasks_str = open('tasks.json', 'rb').read()
    tasks_json = json.loads(tasks_str)

    # Connect to database
    db = dataset.connect('sqlite:///ctf.db')
    cat_table = db.create_table('categories', primary_id=False)
    tasks_table = db.create_table('tasks', primary_id=False)
    cat_task_table = db.create_table('cat_task', primary_id=False)

    # Setup tables at first execution
    if 'flags' not in db.tables:
        db.query('''create table flags (
            task_id INTEGER,
            user_id INTEGER,
            score INTEGER,
            timestamp BIGINT,
            PRIMARY KEY (task_id, user_id))''')
    user_found = db['users'].find_one(username='root')
    if not user_found:
        root_user = dict(hidden=1, username=time.strftime("%Y/%m/%d-%H:%M:%S", time.gmtime()), sno='root')
        db['users'].insert(root_user)
    if 'achivements' not in db.tables:
        db.query('''create table achivements (
            achi_id INTEGER,
            user_id INTEGER,
            PRIMARY KEY (achi_id, user_id))''')

    # Parse the json file and add rows to the table
    old_cat_count = len(list(cat_table))
    old_task_count = len(list(tasks_table))

    # First, create categories
    for category in tasks_json['categories']:

        cat = category.copy()
        del cat['tasks']

        if cat_table.find_one(id=cat['id']):

            # Update existing category
            cat_table.update(cat, ['id'])

        else:
            cat_table.insert(cat)

    new_cat_count = len(list(cat_table))
    print("[*] Imported %d new categories" % (new_cat_count - old_cat_count))

    # Then create tasks
    for category in tasks_json['categories']:
        for task in category['tasks']:

            if tasks_table.find_one(id=task['id']):

                # Update existing table
                tasks_table.update(task, ['id'])
            else:
                tasks_table.insert(task)

                # In this case, we should add an entry to the category_task table as well
                row = dict(cat_id=category['id'], task_id=task['id'])
                cat_task_table.insert(row)

    new_task_count = len(list(tasks_table))
    print("[*] Imported %d new tasks" % (new_task_count - old_task_count))
