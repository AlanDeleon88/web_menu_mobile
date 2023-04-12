from app.models import db, Restaurant


# Adds a demo user, you can add other users here if you want
def seed_restaurant():
     #* menu can be divided to sushi bar, kitchen, drinks, and lunch specials
    huku = Restaurant(
        name='Huku', owner_id=1, description='Japanese restaurant'
    )

    db.session.add(huku)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_restaurant():
    db.session.execute('DELETE from restaurants;')
    db.session.commit()
