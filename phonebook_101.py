import pg

# db = pg.DB(dbname='phonebook_app2')
# query = db.query('select * from phonebook')
# result_list = query.namedresult()

# CREATE TABLE phonebook (
#   id serial PRIMARY KEY,
#   name varchar NOT NULL UNIQUE,
#   email varchar UNIQUE,
#   work_number varchar,
#   home_number varchar,
#   cell_number varchar
# );

def select_data():
    db = pg.DB(dbname='phonebook_app2')
    query = db.query('select * from phonebook')
    result_list = query.namedresult()
    if choice == 1:
        lookup_entry(result_list)
    elif choice == 2:
        add_entry(db, query)
    elif choice == 3:
        delete_entry(db, result_list)
    else:
        print_all_entries(result_list)

def lookup_entry(result_list):
    name = raw_input("\nName? ")
    is_found = False
    for result in result_list:
        if result.name == name:
            print "\nFound entry for %s" % result.name
            print "Email: %s" % result.email
            print "Work Number: %s" % result.work_number
            print "Home Number: %s" % result.home_number
            print "Cell Number: %s" % result.cell_number
            is_found = True
            break
    if is_found == False:
        print "%s does not exist." % name
    else:
        pass

def add_entry(db, query):
    name = raw_input("\nName? ")
    email = raw_input("Email? ")
    work_number = raw_input("Work number? ")
    home_number = raw_input("Home number? ")
    cell_number = raw_input("Cell number? ")
    db.insert('phonebook', name = name, email = email, work_number = work_number, home_number = home_number, cell_number = cell_number)
    print "Entry stored for %s." % name

def delete_entry(db, result_list):
    name = raw_input("\nName? ")
    is_found = False
    for result in result_list:
        if result.name == name:
            entry_id = result.id
            db.delete('phonebook', {'id': entry_id})
            print "Deleted entry for %s" % name
            is_found = True
            break
    if is_found == False:
        print "%s does not exist." % name
    else:
        pass

def print_all_entries(result_list):
    for result in result_list:
        print "\nFound entry for %s: " % result.name
        print "Email: %s" % result.email
        print "Work Number: %s" % result.work_number
        print "Home Number: %s" % result.home_number
        print "Cell Number: %s \n" % result.cell_number

while True:
    print "\nElectronic Phone Book"
    print "====================="

    print "1. Look up an entry"
    print "2. Set an entry"
    print "3. Delete an entry"
    print "4. List all entries"
    print "5. Quit"

    choice = int(raw_input("\nWhat do you want to do? "))

    if choice >= 1 and choice <= 4:
        print "I am inside"
        select_data()
    elif choice == 5:
        print "Bye"
        break
    else:
        # Prompt user to select from the menu or exit the session
        print "Please choose a list from the following or pick 6 to quit."
