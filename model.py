from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Class (Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    level = Column(Integer)
    address = Column(String(50))
    class_teachers = relationship('ClassTeacher', backref="class")
    students = relationship("Student", backref="class")


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    adress = Column(String(50))
    class_id = Column(Integer, ForeignKey('class.id'))


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(10))
    telephone = Column(String(50))
    adress = Column(String(50))

    class_teacher = relationship("ClassTeacher", backref='teacher')


class ClassTeacher(Base):
    __tablename__ = "class_teacher"
    teacher_id = Column(Integer, ForeignKey(
        "teacher.teacher_id"), primary_key=True)
    class_id = Column(Integer, ForeignKey("class.id"), primary_key=True)
