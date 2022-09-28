import psycopg2
def store_passwords(password, user_email, username, url, app_name):

    try:
        connection = psycopg2.connect(user='postgres', password='password123', host='127.0.0.1', port='5432', database='password_manager')
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s) """
        record_to_insert = ('password', 'user_email', 'username', 'url', 'app_name')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount()
        print(count, 'record inserted!')
    except (Exception, psycopg2.Error) as error:
        print(error)

store_passwords()
