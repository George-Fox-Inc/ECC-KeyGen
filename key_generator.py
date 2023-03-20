import curve_point_gen
import help_desk
from random import randint

def key_generation(Fp):
    a = 0
    b = 7
    private_key = randint(1, Fp)
    generator_G = curve_point_gen.Point(int('79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798', 16),
        int('483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8', 16))
    curve = curve_point_gen.Curve(Fp, generator_G, a, b)
    public_key = help_desk.double_add(curve, generator_G, private_key)

    print("Private Key: " + hex(private_key))
    print("Public Key: (" + hex(public_key.x) + ", " + hex(public_key.y) + ")")

key_generation(int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F', 16))



