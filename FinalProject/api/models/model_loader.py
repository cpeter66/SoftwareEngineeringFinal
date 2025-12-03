from . import customers, menu_items, order_items, payments, promotions, resources, reviews

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    payments.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)