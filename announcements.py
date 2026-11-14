import db

def add_announcement(title, description, vähimmäismäärä, user_id):
    sql = "INSERT INTO announcements (title, description, vähimmäismäärä, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, description, vähimmäismäärä, user_id])

def get_announcements():
    sql = "SELECT id, title FROM announcements ORDER BY id DESC"
    return db.query(sql)

def get_announcement(announcement_id):
    sql = """SELECT announcements.id, announcements.title, announcements.description, announcements.vähimmäismäärä, announcements.user_id, users.username
             FROM announcements, users
             WHERE announcements.user_id = users.id AND announcements.id = ?"""
    return db.query(sql, [announcement_id])[0]

def update_announcement(announcement_id, title, description, vähimmäismäärä):
    sql = """UPDATE announcements SET title = ?, description = ?, vähimmäismäärä = ?
    WHERE id = ?"""

    db.execute(sql, [title, description, vähimmäismäärä, announcement_id])

def remove_announcement(announcement_id):
    sql = "DELETE FROM announcements WHERE id = ?"

    db.execute(sql, [announcement_id])

