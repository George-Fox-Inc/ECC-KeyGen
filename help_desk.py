import curve_point_gen
import base64


def infinity_add(curve, point_one, point_two):
    if point_one is curve.id_ele:  # I've added a special case for if one of the points is the point of infinity
        point_one.rewrite(point_two)  # if one of the points is infinity (beginning of the loop) it must be rewritten
    elif point_two is curve.id_ele:
        point_two.rewrite(point_one)


def inverse(curve, point):
    temp_point = curve_point_gen.Point(point.x, (-point.y % curve.p)) # finds the modular inverse of a point
    return temp_point


def point_validity(curve, point):
    return point.y**2 % curve.p == (point.x**3 + curve.a * point.x + curve.b) % curve.p

def inverse_mod(curve, x_coordinate):
    if x_coordinate % curve.p == 0:
        print("mod inverse not possible")
    return pow(x_coordinate, curve.p - 2, curve.p)

def encryption(key):
    if hasattr(key, 'x'):
        x = key.x
        y = key.y
        pubkey_bytes = x.to_bytes(32, byteorder = 'big') + y.to_bytes(32, byteorder = 'big')
        return base64.b64encode(pubkey_bytes)
    else:
        privkey_bytes = key.to_bytes(64, byteorder = 'big')
        return base64.b64encode(privkey_bytes)

def point_add(curve, point_one, point_two):
    gradient = 0
    if point_one == curve.id_ele:
        return point_two
    elif point_two == curve.id_ele:
        return point_one
    elif point_two == inverse(curve, point_one):
        return curve.id_ele
    else:
        if point_one == point_two:
            gradient = (3 * (point_one.x**2) + curve.a) * inverse_mod(curve, (2 * point_one.y))
        if point_one != point_two:
            gradient = (point_two.y - point_one.y) * inverse_mod(curve, (point_two.x - point_one.x))

    x3 = (gradient ** 2 - point_one.x - point_two.x) % curve.p
    y3 = (gradient * (point_one.x - x3) - point_one.y) % curve.p

    point_three = curve_point_gen.Point(x3, y3)  # creates the third point
    return point_three


def double_add(curve, generator_point, priv_key):
    binary_key = bin(priv_key)[3:]
    key_arr = [char for char in binary_key]
    public_key = curve_point_gen.Point(0, 0)
    public_key.rewrite(generator_point)

    for i in range(len(key_arr)): # Double-Add algorithm doubles and adds if the bit of the multiplication number is 1, just doubles if the bit is 0
        public_key = point_add(curve, public_key, public_key)  # doubles P
        if int(key_arr[i]) == 1:
            public_key = point_add(curve, curve.g, public_key)  # adds P to nP

    return public_key

