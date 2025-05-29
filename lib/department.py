from db import CONN, CURSOR

class Department:
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name} ({self.location})>"

    # --------- CREATE TABLE ----------
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    # --------- DROP TABLE ----------
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS departments"
        CURSOR.execute(sql)
        CONN.commit()

    # --------- SAVE ----------
    def save(self):
        if self.id is None:
            sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
            CURSOR.execute(sql, (self.name, self.location))
            CONN.commit()
            self.id = CURSOR.lastrowid
            self.__class__.all[self.id] = self
        else:
            self.update()

    # --------- CREATE ----------
    @classmethod
    def create(cls, name, location):
        dept = cls(name, location)
        dept.save()
        return dept

    # --------- UPDATE ----------
    def update(self):
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    # --------- DELETE ----------
    def delete(self):
        sql = "DELETE FROM departments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del self.__class__.all[self.id]

    # --------- FIND BY ID ----------
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM departments WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            id, name, location = row
            dept = cls(name, location, id)
            cls.all[id] = dept
            return dept
        return None

    # --------- GET ALL ----------
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM departments"
        rows = CURSOR.execute(sql).fetchall()
        departments = []
        for row in rows:
            id, name, location = row
            dept = cls(name, location, id)
            cls.all[id] = dept
            departments.append(dept)
        return departments
