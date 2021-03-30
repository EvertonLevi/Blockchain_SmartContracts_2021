from datetime import datetime
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import binascii
import collections
from client import Client

# TODO implementar a lógica de fila nas transações


class Transaction:

    transacoes = []

    seller = Client()
    buyer = Client()

    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.now()

    def display_transaction(transaction):
        dict = transaction.to_dict()
        print("Pagador: " + dict['sender'])
        print('"-----"')
        print("Recebedor: " + dict['recipient'])
        print('"-----"')
        print("Valor: " + str(dict['value']))
        print('"-----"')
        print("Hora: " + str(dict['time']))
        print('"-----"')

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
