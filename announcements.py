import db

def add_announcement(title, description, vähimmäismäärä, user_id):
    sql = "INSERT INTO announcements (title, description, vähimmäismäärä, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, description, vähimmäismäärä, user_id])

def get_announcements():
    sql = "SELECT id, title FROM announcements ORDER BY id DESC"

    return db.query(sql)

def get_announcement(announcement_id):
    sql = """SELECT announcements.title, announcements.description, announcements.vähimmäismäärä, users.username
             FROM announcements, users
             WHERE announcements.user_id = users.id AND announcements.id = ?"""
    return db.query(sql, [announcement_id])[0]
