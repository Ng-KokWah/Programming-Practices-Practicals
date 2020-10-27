from tkinter import *
import sqlite3

root = Tk()
root.title("Database App")
root.geometry("360x400")

# 1. create/connect to database, if it does not exists it would create it, else it would just connect to it
# it would create this database file in the directory that you saved the project in
conn = sqlite3.connect('address_book.db')

# 2. create cursor
c = conn.cursor()

# 3. create table (ONLY RUN THIS ONCE)
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''
# c.execute("DROP TABLE addresses")


def update():
    # connect to database
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode= :zipcode
        
        WHERE oid = :oid""",
        {'first': f_name_editor.get(),
         'last': l_name_editor.get(),
         'address': address_editor.get(),
         'city': city_editor.get(),
         'state': state_editor.get(),
         "zipcode": zipcode_editor.get(),
         'oid': record_id
        })

    # this commits or saves the changes to the database
    conn.commit()

    # close database connection
    conn.close()

    editor.destroy()


def edit():
    # connect to database
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    # query the database
    # the oid is the default primary key created automatically by sqlite
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)

    records = c.fetchall()

    global editor
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("360x400")

    # create global variable for textbox names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # create textboxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # create textbox label
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor = Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)

    # save button
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # close database connection
    conn.close()


def delete():
    # connect to database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())

    # this commits or saves the changes to the database
    conn.commit()

    # close database connection
    conn.close()


def submit():
    # connect to database
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()
    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get(),
              })

    # clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # this commits or saves the changes to the database
    conn.commit()

    # close database connection
    conn.close()


def query():
    # connect to database
    conn = sqlite3.connect('address_book.db')

    # create cursor
    c = conn.cursor()

    # query the database
    # the oid is the default primary key created automatically by sqlite
    c.execute("SELECT *, oid FROM addresses")
    # 6. .fetchone get one record, .fetchmany() you can specify how many to get back
    # .fetchall just gets everything but returns it in the form of a list, with tuples
    records = c.fetchall()

    print_records = ''
    ''' Display everything
    for record in records:
        for r in record:
            print_records += str(r) + "\n"
    '''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # this commits or saves the changes to the database
    conn.commit()

    # close database connection
    conn.close()


# create textboxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# create textbox label
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0)

# create submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# create a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# create a delete button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# 4. this commits or saves the changes to the database
conn.commit()

# 5. close database connection
conn.close()

root.mainloop()
