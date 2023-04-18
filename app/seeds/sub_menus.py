from app.models import db, SubMenu


# Adds a demo user, you can add other users here if you want
def seed_sub_menu():
    #* Kitchen -> 1, Sushi --> 2, Lunch SP -> 3, Drinks -> 4
    
    appetizers = SubMenu(
        name='Appetizers', menu_id = 1, description ='Dishes for sharing before your entrees.'
        )

    freshAndRaw = SubMenu(
        name='Fresh and Raw', menu_id = 2, description = 'Our dishes with fresh and raw ingredients'
    )

    nigiri = SubMenu(
        name = 'Nigiri', menu_id = 2, description = 'Our selection of fresh fish for nigiri'
    )

    sashimi = SubMenu(
        name ='Sashimi', menu_id = 2, description = 'Our Selection of fresh fish for sashimi'
    )

    salads = SubMenu(
        name = 'Salads', menu_id = 2, description = 'Salads'
    )

    udonRamen = SubMenu(
        name = 'Udon and Ramen', menu_id = 1, description = 'Our ramen and udon, all broths have dashi(fish) base'
    )

    donburi = SubMenu(
        name = 'Donburi', menu_id = 1, description = 'Our rice bowls'
    )

    lunchEntreeKitchen = SubMenu(
        name = 'Lunch Entree Kitchen', menu_id = 1, description = 'Lunch entrees from the kitchen served from open to 3pm'
    )

    lunchEntreeSushi = SubMenu(
        name = 'Lunch Entree Sushi', menu_id = 2, description = 'Lunch entrees from the sushi bar, from open to 3pm'
    )

    dinnerEntreeKitchen = SubMenu(
        name = 'Dinner Entree', menu_id = 1, description = 'Dinner entrees from the kitchen served all day'
    )

    dinnerEntreeSushi = SubMenu(
        name = 'Dinner Entree', menu_id = 2, description = 'Dinner entrees from the sushi bar served all day'
    )

    classicRolls = SubMenu(
        name = 'Classic Rolls', menu_id = 2, description = 'more traditional rolls. 6 pieces'
    )

    HouseRolls = SubMenu(
        name = 'House Rolls', menu_id = 2, description = 'Our house rolls, 8 pieces.'
    )

    noAlchohol = SubMenu(
        name = 'Non Alcoholic drinks', menu_id = 2, description = "Soda's and juices"
    )

    beer = SubMenu(
        name = 'Beer', menu_id = 4, description = "Bottled Beers"
    )

    wine = SubMenu(
        name = 'Wine', menu_id = 4, description = "Our wine selection avaliable by glass or bottle"
    )

    sake = SubMenu(
        name = "Sake", menu_id = 4, description = "Our selection of sake"
    )

    db.session.add(appetizers)
    db.session.add(freshAndRaw)
    db.session.add(nigiri)
    db.session.add(sashimi)
    db.session.add(salads)
    db.session.add(udonRamen)
    db.session.add(donburi)
    db.session.add(lunchEntreeKitchen)
    db.session.add(dinnerEntreeKitchen)
    db.session.add(lunchEntreeSushi)
    db.session.add(dinnerEntreeSushi)
    db.session.add(classicRolls)
    db.session.add(HouseRolls)
    db.session.add(noAlchohol)
    db.session.add(beer)
    db.session.add(wine)
    db.session.add(sake)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_sub_menu():
    db.session.execute('DELETE from sub_menus;')
    db.session.commit()
