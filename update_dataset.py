import sqlite3

# SRC_DB = "/home/balor/Workspace/workspace/projects/Review_Scraper/reviews.db"
SRC_DB = "/home/balor/Workspace/workspace/projects/Review_Scraper/yelp_neg_reviews.db"
DEST_DB = "./db.sqlite3"

conn1 = sqlite3.connect (SRC_DB)
curr1 = conn1.cursor()
conn2 = sqlite3.connect (DEST_DB)
curr2 = conn2.cursor()

curr1.execute ("SELECT text from neg_reviews;")
# curr1.execute ("SELECT text from reviews;")
rows = curr1.fetchall()

count = 0
for row in rows:
    row = row[0].replace("<br>", " <br> ");
    curr2.execute (f"""INSERT INTO review_review(review_text,sentiment) VALUES("{row}", 200);""")
    # curr2.execute (f"""INSERT INTO review_review(review_text,sentiment) VALUES("{row}", 100);""")
    print (count)
    count += 1
    conn2.commit()

conn1.close()
conn2.close()
