import sqlite3

class DBcon:    # DB actions class

    def __init__(self, database_name='test.db'):  # setting db name
        with sqlite3.connect(database_name) as self.conn:  # creating connection
            self.cur = self.conn.cursor()  # initializing cursor

    def select(self, table_name):  # select method
        self.cur.execute(f'SELECT * FROM {table_name}')
        return self.cur.fetchall()  # executing commands in the cursor

    def insert_news(self, date, city, text, table_name='news'):  # inserting news method
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (news_date datetime, news_city text UNIQUE, news_text text)") # creating table and setting INIQUE constraint to text of the post
        self.cur.execute(f"INSERT INTO {table_name} VALUES ('{date}', '{city}', '{text}')")  # inserting values
        self.conn.commit()  # commit
        self.cur.fetchall()  # executing

    def insert_ads(self, date, text, actual_until, table_name='privatead'):  # inserting ads method
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (ad_date datetime, ad_text UNIQUE, actual_until_date text)")  # creating table and setting INIQUE constraint to text of the ad
        self.cur.execute(f"INSERT INTO {table_name} VALUES ('{date}', '{text}', '{actual_until}')")  # inserting values
        self.conn.commit()  # commit
        self.cur.fetchall()  # executing

    def insert_obituary(self, date, city, ob_text, burial_date, burial_place, table_name='obituary'):  # inserting obituary method
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (date datetime, city text, ob_text text UNIQUE, burial_date datetime, burial_place text)")  # creating table and setting UNIQUE constraint to text of the obituary
        self.cur.execute(f"INSERT INTO {table_name} VALUES ('{date}', '{city}', '{ob_text}', '{burial_date}', '{burial_place}')")  # inserting values
        self.conn.commit()  # commit
        self.cur.fetchall()  # executing

    def drop_table(self, table_name):  # function to drop table
        self.cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.conn.commit()  # commit
        self.cur.fetchall()  # executing

    def close_all(self):  # closing cursor and connection
        self.cur.close()
        self.conn.close()
