import db

def add_announcement(title, description, vähimmäismäärä, user_id):
    sql = "INSERT INTO announcements (title, description, vähimmäismäärä, user_id) VALUES (?, ?, ?, ?)"
    db.execute(sql, [title, description, vähimmäismäärä, user_id])

def get_announcements():
    sql = "SELECT id, title FROM announcements ORDER BY id DESC"
    return db.query(sql)

def get_user_announcements(user_id):
    sql = "SELECT id, title FROM announcements WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql, [user_id])

def get_announcement(announcement_id):
    sql = """SELECT announcements.id, announcements.title, announcements.description, announcements.vähimmäismäärä, announcements.user_id, users.username
             FROM announcements, users
             WHERE announcements.user_id = users.id AND announcements.id = ?"""
    result = db.query(sql, [announcement_id])
    return result[0] if result else None

def update_announcement(announcement_id, title, description, vähimmäismäärä):
    sql = """UPDATE announcements SET title = ?, description = ?, vähimmäismäärä = ?
    WHERE id = ?"""

    db.execute(sql, [title, description, vähimmäismäärä, announcement_id])

def remove_announcement(announcement_id):
    sql = "DELETE FROM announcements WHERE id = ?"

    db.execute(sql, [announcement_id])

def find_announcements(query):
    sql = """SELECT id, title
             FROM announcements
             WHERE title LIKE ? OR description LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

