import psycopg2

# AWS Redshift connection details
host = ''
port = '5439'
database = ''
user = ''
password = ''

# Establish connection
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute('SELECT * FROM your_table TOP 3')
rows = cursor.fetchall()

# Process the results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()