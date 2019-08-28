import datetime
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    status = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow())
    todo_list_id = Column(Integer, ForeignKey('todo_lists.id'))
    todo_list = relationship('TodoList', back_populates='tasks')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<Task: id={self.id} description={self.description}>'


class TodoList(Base):
    __tablename__ = 'todo_lists'
    id = Column(Integer, primary_key=True)
    label = Column(String)
    tasks = relationship('Task', back_populates='todo_list'
                         , cascade="all, delete, delete-orphan")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<TodoList: id={self.id} label={self.label}>'
