import mysql.connector

cnx = mysql.connector.connect(user='gabriel', password='gabriel123456789',
                              host='aurorahorizon.ddns.net',
                              )

print(cnx)