from app.config import db, app
# import os,sys
# sys.path.insert(1, os.path.join(sys.path[0], '../'))
# from config import app, db

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    chatId = db.Column(db.BigInteger, nullable=False)
    language = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(64), nullable=True)
    dateLogin = db.Column(db.String(64), default="N/A")
    refCode = db.Column(db.String(64), default="N/A")
    location = db.Column(db.String, nullable=True)
    comment = db.Column(db.String, nullable=True)
    contact = db.Column(db.String, nullable=True)
    # cart = db.Column(db.PickleType)

    def __repr__(self):
        return '<Account %r>' % self.username

def addCustomer(chatId: int, username: str, dateLogin: str):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                return 0
            else:
                customer = Customer(chatId=chatId, username=username, dateLogin=dateLogin,
                                    language='RU')
                db.session.add(customer)
                db.session.commit()

            return 1
    except Exception as e:
        return print(e, "\naddCustomer error")

def getCustomer(chatId: int):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                return customer
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\ngetCustomer error")

def getAllCustomers():
    try:
        with app.app_context():
            x = list(map(lambda x: x, Customer.query.filter(Customer.id is not None).all()))
            return x

    except Exception as e:
        return print(e, "\ngetAllCustomers error")


def setRef(chatId, refCode):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                customer.refCode = refCode
                db.session.commit()
                return {"message": f'Language set is{customer.language}', "status": True}
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\nsetLanguage error")
def getRef(chatId):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                return customer.refCode
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\ngetLanguage error")

def setLanguage(chatId, language):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                customer.language = language
                db.session.commit()
                return {"message": f'Language set is{customer.language}', "status": True}
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\nsetLanguage error")

def getLanguage(chatId):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                return customer.language
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\ngetLanguage error")

def setAddress(chatId, location):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                customer.location = location
                db.session.commit()
                return {"message": f'Location set is{customer.location}', "status": True}
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\nsetAddress error")

def getAddress(chatId):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                return customer.location
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\nsetAddress error")

def setComment(chatId, comment):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                customer.comment = comment
                db.session.commit()
                return {"message": f'Location set is{customer.location}', "status": True}
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\nsetAddress error")

def getComment(chatId):
    try:
        with app.app_context():
            if Customer.query.filter_by(chatId=chatId).first():
                customer = Customer.query.filter_by(chatId=chatId).first()
                return customer.comment
            else:
                return {"message": 'No user with this chatId', "status": False}

    except Exception as e:
        return print(e, "\nsetAddress error")

# def setProduct(chatId, nameOfProduct, numOfProduct, priceOfProduct):
#     try:
#         with app.app_context():
#             if Customer.query.filter_by(chatId=chatId).first():
#                 customer = Customer.query.filter_by(chatId=chatId).first()
#                 customer.cart[nameOfProduct] = numOfProduct
#                 db.session.commit()
#                 return {"message": f'Location set is{customer.location}', "status": True}
#             else:
#                 return {"message": 'No user with this chatId', "status": False}
#
#     except Exception as e:
#         return print(e, "\nsetProduct error")
#
# def getCart(chatId):
#     try:
#         with app.app_context():
#             if Customer.query.filter_by(chatId=chatId).first():
#                 customer = Customer.query.filter_by(chatId=chatId).first()
#                 return customer.cart
#             else:
#                 return {"message": 'No user with this chatId', "status": False}
#
#     except Exception as e:
#         return print(e, "\nsetAddress error")
#
# def getOfNumberOfProducts(chatId):
#     try:
#         with app.app_context():
#             if Customer.query.filter_by(chatId=chatId).first():
#                 customer = Customer.query.filter_by(chatId=chatId).first()
#                 return len(customer.cart)
#             else:
#                 return {"message": 'No user with this chatId', "status": False}
#
#     except Exception as e:
#         return print(e, "\ngetOfNumberOfProducts error")
# def setContact(chatId, contact):
#     try:
#         with app.app_context():
#             if Customer.query.filter_by(chatId=chatId).first():
#                 customer = Customer.query.filter_by(chatId=chatId).first()
#                 customer.contact = contact
#                 db.session.commit()
#                 return {"message": f'Location set is{customer.location}', "status": True}
#             else:
#                 return {"message": 'No user with this chatId', "status": False}
#
#     except Exception as e:
#         return print(e, "\nsetAddress error")
#
# def getContact(chatId):
#     try:
#         with app.app_context():
#             if Customer.query.filter_by(chatId=chatId).first():
#                 customer = Customer.query.filter_by(chatId=chatId).first()
#                 return customer.contact
#             else:
#                 return {"message": 'No user with this chatId', "status": False}
#
#     except Exception as e:
#         return print(e, "\nsetAddress error")






