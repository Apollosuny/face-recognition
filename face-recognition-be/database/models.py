from sqlalchemy import BigInteger, DateTime, Identity, PrimaryKeyConstraint, Column, String, ForeignKey, Enum, LargeBinary
from sqlalchemy.orm import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100))
    phone = Column(String(20))
    address = Column(String(200))
    role = Column(Enum('student', 'lecturer', 'superadmin'), default='student')

class Face(base):
    __tablename__ = 'face'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    face_data = Column(LargeBinary)
    user_id = Column(BigInteger, ForeignKey('user.id'))

class Attendance(base):
    __tablename__ = 'attendance'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id'))
    check_in_at = Column(DateTime)
