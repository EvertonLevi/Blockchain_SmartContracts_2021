import hashlib
from client import Client
from transaction import Transaction
# from bloco import Bloco

if __name__ == '__main__':

    seller = Client()
    buyer = Client()
    transactions = []

    t = Transaction(
        seller,
        buyer.identity,
        5.0
    )

    t1 = Transaction(
        seller,
        buyer.identity,
        15.0
    )

    t2 = Transaction(
        seller,
        buyer.identity,
        6.0
    )

    t3 = Transaction(
        seller,
        buyer.identity,
        4.0
    )

    t4 = Transaction(
        seller,
        buyer.identity,
        11.0
    )

    t5 = Transaction(
        seller,
        buyer.identity,
        6.0
    )

    t6 = Transaction(
        seller,
        buyer.identity,
        69.0
    )

    t7 = Transaction(
        seller,
        buyer.identity,
        6.0
    )

    t.sign_transaction()
    t1.sign_transaction()
    t2.sign_transaction()
    t3.sign_transaction()
    t4.sign_transaction()
    t5.sign_transaction()
    t6.sign_transaction()
    t7.sign_transaction()

    transactions.append(t)
    transactions.append(t1)
    transactions.append(t2)
    transactions.append(t3)
    transactions.append(t4)
    transactions.append(t5)
    transactions.append(t6)
    transactions.append(t7)

    for transaction in transactions:
        Transaction.display_transaction(transaction)
        print('-------------------------------')
