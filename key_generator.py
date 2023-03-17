import curve_point_gen
import help_desk
from random import randint

def key_generation(Fp):
    a = 0
    b = 7
    priv_key = randint(1, Fp)
    generator_G = curve_point_gen.Point(int('79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798', 16),
        int('483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8', 16))
    curve = curve_point_gen.Curve(Fp, generator_G, a, b)
    public_key = help_desk.double_add(curve, generator_G, priv_key)

    pubkey_b64 = help_desk.encryption(public_key)
    pem_pubkey = "-----BEGIN PUBLIC KEY-----\n"
    pem_pubkey += pubkey_b64.decode('utf-8') + "\n"
    pem_pubkey += "-----END PUBLIC KEY-----\n"
    print(pem_pubkey)
    #print("Coefficient: "+ str(hex(priv_key)))
    #print("Final point and public key: (" + str(hex(public_key.x)) + ", " + str(hex(public_key.y)) + ")")
    return priv_key, public_key

key_generation(int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F', 16))


