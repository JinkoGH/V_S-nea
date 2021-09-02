import sqlite3
con = sqlite3.connect('Database test.db')
cursor=con.cursor()
#cursor.execute('CREATE TABLE components (rowid int,name varchar(50))')
cursor.execute('INSERT INTO components values(?,?)', (2,'doo',))
con.commit()


for name in ('bar','foo','doo'):
    cursor.execute("SELECT rowid FROM components WHERE name = ?", (name,))
    data=cursor.fetchone()
    if data is None:
        print('There is no component named %s'%name)
    else:
        print('Component %s found with rowid %s'%(name,data[0]))