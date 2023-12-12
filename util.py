
import re
def prepend_database_name(sql_query, database_name):
    # This regular expression finds the table name in the SQL query.
    # It assumes that the table name is preceded by 'FROM ' or 'JOIN ' and 
    # followed by a space, comma or end of string.
    pattern = re.compile(r'(?<=FROM |JOIN )\w+(?=[ ,\n]|$)', re.IGNORECASE)

    # This function takes a match object and returns the table name 
    # prepended with the database name and a dot.
    def replacer(match):
        return f'{database_name}.{match.group(0)}'

    # Use the sub method to replace all table names in the SQL query.
    return pattern.sub(replacer, sql_query)