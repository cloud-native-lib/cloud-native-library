import logging

def get_title(conn):
    
    cursor = conn.cursor(dictionary=True)
    request = """
    SELECT titre
    FROM library
    WHERE id=(SELECT max(id) FROM library);
    """
    cursor.execute(request)
    return cursor.fetchone()['titre']

def load_info(conn, info):

    cursor = conn.cursor(dictionary=True)
    values = (info, get_title(conn))
    request = """
    UPDATE library
    SET info = %s
    WHERE titre = %s
    """
    logging.info(f"info: {info}, title: {get_title(conn)}")
    cursor.execute(request, values)
    conn.commit()
