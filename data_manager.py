import database_connector


@database_connector.connection_handler
def get_all_applicants_first_name(cursor):
    cursor.execute(f"""
                    SELECT first_name, id FROM applicants;
    """)
    applicants = cursor.fetchall()
    return applicants


@database_connector.connection_handler
def get_applicant_info(cursor, applicant_id):
    cursor.execute(f"""
                    SELECT * FROM applicants WHERE id = {applicant_id};
    """)
    applicant = cursor.fetchone()
    return applicant
