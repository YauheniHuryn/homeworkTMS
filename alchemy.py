import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates,declarative_base

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'

    customer_id = sa.Column(sa.Integer, primary_key=True, autoincrement = False)
    name = sa.Column(sa.Text, nullable = False)
    address = sa.Column(sa.Text, nullable = True)
    contact = sa.Column(sa.Text, nullable = False)


class Orders(Base):
    __tablename__ = 'orders'

    order_id = sa.Column(sa.Integer,primary_key=True, autoincrement=False)
    customer_id = sa.Column(sa.Integer, sa.ForeignKey('customers.customer_id'), nullable=False)
    date = sa.Column(sa.Date, nullable=False)


class Products(Base):
    __tablename__ = 'products'

    product_id = sa.Column(sa.Integer, primary_key=True)
    product_name = sa.Column(sa.Text, nullable = False)
    price = sa.Column(sa.Float, nullable = False)

class OrderDetails(Base):
    __tablename__ = 'orderdetails'

    product_id = sa.Column(sa.Integer,  sa.ForeignKey('products.product_id'), primary_key=True, nullable=False)
    order_id = sa.Column(sa.Integer, sa.ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    quantity = sa.Column(sa.Integer, nullable = False)


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://yauhen:test@localhost:5432/database1')
Base.metadata.create_all(engine)


