import sqlite3
conn = sqlite3.connect('db/member.db')
cursor = conn.cursor()
sql = "SELECT * FROM login WHERE user='art';"
cursor.execute(sql)
# result = cursor.fetchall()
# print(result[0][2]+" "+ result[0][3])
result = cursor.fetchone()
print(result[2]+" "+result[3])
cursor.close()
conn.close()