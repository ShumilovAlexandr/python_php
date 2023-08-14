import datetime

from sqlalchemy import (Table,
                        Column,
                        MetaData,
                        Integer,
                        BigInteger,
                        String,
                        Float,
                        Time,
                        Date,
                        ForeignKey,
                        DateTime)
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship)


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=True)
    ref_user_id = Column(Integer, ForeignKey("users.id"))
    registration_date = Column(Date,
                               default=datetime.datetime.now().date(),
                               nullable=False)


# delayed_posts = Table(
#     "delayed_posts",
#     metadata,
#     Column("rowid", Integer, primary_key=True, autoincrement=True),
#     Column("chatid", Integer, nullable=False),
#     Column("send_date_time", DateTime, nullable=False),
#     Column("stop", Integer, nullable=False)
# )


# balance = Table(
#     "balance",
#     metadata,
#     Column("rowid", Integer, primary_key=True, autoincrement=True),
#     Column("userid", Integer, nullable=False),
#     Column("sum", Float, nullable=False)
# )


# orders = Table(
#     "orders",
#     metadata,
#     Column("row_id", Integer, primary_key=True, autoincrement=True),
#     Column("chat_id", Integer, nullable=False),
#     Column("service_id", Integer, nullable=False),
#     Column("volume", Integer, nullable=False),
#     Column("sum", Float, nullable=False),
#     Column("times", Time, nullable=False),
#     Column("status", Integer, nullable=False),
#     Column("smo_order_id", BigInteger, nullable=False)
# )


# paylinks = Table(
#     "paylinks",
#     metadata,
#     Column("rowid", Integer, primary_key=True, autoincrement=True),
#     Column("chatid", Integer, nullable=False),
#     Column("times", Time, nullable=False),
#     Column("status", Integer, nullable=False),
#     Column("sum", Float, nullable=False)
# )
#
#
# smoservices = Table(
#     "smoservices",
#     metadata,
#     Column("rowid", Integer, primary_key=True, autoincrement=True),
#     Column("id", Integer, nullable=False),
#     Column("name", TEXT(250), nullable=False),
#     Column("min", Integer, nullable=False),
#     Column("max", BigInteger, nullable=False),
#     Column("price", Float, nullable=False),
#     Column("category_id", Integer, nullable=False),
#     Column("code", String(250), nullable=False)
# )
#
#
# tempsess = Table(
#     "tempsess",
#     metadata,
#     Column("rowid", Integer, primary_key=True, autoincrement=True),
#     Column("chat_id", Integer, nullable=False),
#     Column("serviceid", Integer, nullable=True),
#     Column("o_tipe", String(64), nullable=True),
#     Column("time", Time, nullable=False),
#     Column("volume", Integer, nullable=True),
#     Column("waitpayment", Integer, nullable=True),
#     Column("page", String(250), nullable=True)
# )
#
