import database_connector


@database_connector.connection_handler
def get_all_applicants_first_name(cursor):
    cursor.execute(f"""
                    SELECT first_name FROM applicants;
    """)
    applicants = cursor.fetchall()
    return applicants
