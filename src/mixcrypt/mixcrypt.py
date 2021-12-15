import phe
import rsa
import torch
import numpy as np

from mixcrypt.util import float_to_binary

phe_public_key, phe_private_key = phe.generate_paillier_keypair()
rsa_public_key, rsa_private_key = rsa.newkeys(3072)

def encrypt(tensor: torch.tensor):
    signs, exponents, mantissas = float_to_binary(np.asarray(tensor))
    encrypted_signs = [phe_public_key.encrypt(val.item()) for val in signs.flatten()]
    encrypted_mantissas = [phe_public_key.encrypt(val.item()) for val in mantissas.flatten()]
    encrypted_exponents = [int.from_bytes(bytestring, 'little') for bytestring in [rsa.encrypt(val.item().to_bytes(2, byteorder='little'), rsa_public_key) for val in exponents.flatten()]]
    return encrypted_signs, encrypted_mantissas, encrypted_exponents
