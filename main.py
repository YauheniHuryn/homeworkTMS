from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from alchemy import OrderDetails, Products

if __name__ == '__main__':
    import sys

    sys.path.append('/home/user/PycharmProjects/databese/data')
    sys.path.append('/home/user/PycharmProjects/databese/infrastructure')

    engine = create_engine('postgresql+psycopg2://yauhen:test@localhost:5432/database1')
    Session = sessionmaker(bind=engine)
    session = Session()

    det17 = OrderDetails(product_id=1000450, order_id=1001, quantity=2)

    session.add_all([det17])
    session.commit()

# need to implement orderdetailsID!!!!!!!!!!