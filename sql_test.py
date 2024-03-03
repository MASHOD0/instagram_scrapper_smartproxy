from DB import db, query as q


conn = db.connect()
# 
# db.execute(conn, q.insert_comment)

rows = db.fetch(conn, q.select_all_platforms)

for row in rows:
    print(row)