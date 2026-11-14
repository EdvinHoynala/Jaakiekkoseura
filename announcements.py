import db

def add_announcement(title, description, vähimmäismäärä, user_id):
    sql = "INSERT INTO announcements (title, description, vähimmäismäärä, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, description, vähimmäismäärä, user_id])