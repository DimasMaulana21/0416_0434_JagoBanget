from project.config.Database import db
from project.config.DatetimeEncoder import DatetimeEncoder
from project.config.Hash import Hash

from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class NewsModel(db.Model):
   __tablename__ = "tbl_news"

   id = db.Column(db.INTEGER, autoincrement=True, primary_key=True) 
   title = db.Column(db.String(255), nullable=False)
   content = db.Column(db.TEXT, nullable=False)
   datetime = db.Column(db.DATETIME, nullable=False, default=datetime.now)
   flag = db.Column(db.INTEGER, nullable=False, default=1)
   created_by = db.Column(db.INTEGER, ForeignKey("tbl_users.id"), nullable=False)
   updated_by = db.Column(db.INTEGER, ForeignKey("tbl_users.id"), nullable=False)

   # creator = relationship("UserModel", backref="")
   # updator = relationship("UserModel", backref=)

class UserModel(db.Model):
    __tablename__ = "tbl_users"

    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True) 
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    read_key = db.Column(db.String(255), nullable=True)
    write_key = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.BOOLEAN, nullable=False, default=1)
