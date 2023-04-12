from app.models import db, Menu


# Adds a demo user, you can add other users here if you want
def seed_menu():
     #* menu can be divided to sushi bar, kitchen, drinks, and lunch specials
    huku_kitchen = Menu(
        name='Kitchen', restaurant_id=1, description='Dishes from the kitchen'
    )
    huku_sushi = Menu(
        name='Sushi bar', restaurant_id=1, description = 'Dishes from the sushibar'
    )

    huku_lunch_sp = Menu(
        name='Lunch Specials', restaurant_id=1, description = 'Lunch specials weekdays from open to 3pm!'
    )

    huku_drink = Menu(
        name='Beverages', restaurant_id = 1, description = 'Drinks'
    )

    db.session.add(huku_kitchen)
    db.session.add(huku_sushi)
    db.session.add(huku_lunch_sp)
    db.session.add(huku_drink)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_menu():
    db.session.execute('DELETE from menus;')
    db.session.commit()
