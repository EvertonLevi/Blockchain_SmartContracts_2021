import binascii
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    
    def __init__(self):
        random = Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        code = binascii.hexlify(self._public_key.exportKey(
            format='DER')).decode('ascii')
        # print('identity client: ', code)
