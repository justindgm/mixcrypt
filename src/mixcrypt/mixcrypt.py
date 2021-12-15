import phe
import rsa
import torch
import numpy as np

from mixcrypt.util import float_to_binary, binary_to_float

phe_public_key, phe_private_key = phe.generate_paillier_keypair()
rsa_public_key, rsa_private_key = rsa.newkeys(3072)

def encrypt(tensor: torch.tensor):
    signs, exponents, mantissas = float_to_binary(np.asarray(tensor))
    encrypted_signs = [rsa.encrypt(val.item().to_bytes(1, 'little'), rsa_public_key) for val in signs.flatten()]
    encrypted_exponents = [phe_public_key.encrypt(val.item()) for val in exponents.flatten()]
    encrypted_mantissas = [rsa.encrypt(val.item().to_bytes(6, 'little'), rsa_public_key) for val in mantissas.flatten()]
    return encrypted_signs, encrypted_exponents, encrypted_mantissas

def decrypt(encrypted_signs, encrypted_exponents, encrypted_mantissas):
    signs = np.asarray([int.from_bytes(bytestring, 'little') for bytestring in [rsa.decrypt(val, rsa_private_key) for val in encrypted_signs]], dtype=np.bool_)
    exponents = np.asarray([phe_private_key.decrypt(val) for val in encrypted_exponents], dtype=np.uint8)
    mantissas = np.asarray([int.from_bytes(bytestring, 'little') for bytestring in [rsa.decrypt(val, rsa_private_key) for val in encrypted_mantissas]], dtype=np.uint32)
    return binary_to_float(signs, exponents, mantissas)