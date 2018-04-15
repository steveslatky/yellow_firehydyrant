import json
import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def main():
    f = open("../data/hydrants.json", "r")
    data = json.load(f)

    conn = create_connection("../database/hydrants.db")

    # c.execute('''CREATE TABLE locations (id int, lat float, lng float, oos bool, note varchar(255));''')

    # {"lat":39.8852,"lng":-75.064254,"OutOfService":false,"Critical":false,"CriticalNotes":null}
    for e, row in enumerate(data):
        _lat = row["lat"]
        _lng = row["lng"]
        _oos = row["Critical"]
        _note = row["CriticalNotes"]
        params = (int(e), float(_lat), float(_lng), bool(_oos), _note)
        conn.execute("INSERT INTO locations VALUES(?,?,?,?,?)", params)
        conn.commit()


if __name__ == '__main__':
    main()
