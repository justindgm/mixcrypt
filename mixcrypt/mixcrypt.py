import phe
import rsa
import torch
import cupy as cp

from mxc.util import float_to_binary

phe_public_key, phe_private_key = phe.generate_paillier_keypair()
rsa_public_key, rsa_private_key = rsa.newkeys(3072)

t = torch.rand((3,3,2))

def encrypt(tensor: torch.tensor):
    signs, exponents, mantissas = float_to_binary(cp.asarray(tensor))
    for val in mantissas.flatten():
        print(val, type(val))
    
    encrypted_mantissas = [phe_public_key.encrypt(val) for val in mantissas.flatten()]
    encrypted_exponents = [rsa.encrypt(val, rsa_public_key) for val in exponents.flatten()]
    return 0

encrypt(t)
