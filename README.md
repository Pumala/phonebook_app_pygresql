# Phonebook App     

#### Making your Python talk to Postgresql

In a prior class assignment, we created a basic phonebook app that allowed
the user to lookup, store, and delete an entry from the phonebook. In that project,
we used pickle to save the information from previous sessions.
In this class assignment, our objective instead was to modify the phonebook and make it
talk to Postgresql.

In order to do that, I first installed PyGreSQL by entering 'pip install6 PyGreSQL'
in the command line. Then in my py file, I connected to a database as such:
```
import pg

db = pg.DB(dbname='database_name_goes_here')
```
At this point, I figured out that my approach required me to constantly connect
to the database and query the data. So then I stored all of that inside of a function:
```
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
```
I also created an if, else statement inside of the function. Depending on the user's
choice, the function called another function and passed in particular information
from the phonebook database.

Once the other function was called, that function was able to use that information
and work with it.
