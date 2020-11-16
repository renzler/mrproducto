# DATABASE CONNECTION STUFF
# from datetime import date, datetime, timedelta
import mysql.connector
config = {
  'user': dbuser,
  'password': dbpass,
  'host': dbhostname,
  'database': dbname,
  'charset': charset,
  'raise_on_warnings': True,
  'buffered': True
}
# cnx = mysql.connector.connect(**config)
# cursor = cnx.cursor()
# cnx.commit()
# cursor.close()
# cnx.close()
