#!/usr/bin/env python


def gcd(ap, bp):
    while bp > 0:
        amb = ap % bp
        ap = bp
        bp = amb
    return ap


def exp(xp, yp, np):
    number = 1
    while yp:
        if yp & 1:
            number = number * xp % np
        yp >>= 1
        xp = xp * xp % np
    return number


def ee(ae, be):
    if be == 0:
        return 1, 0, ae
    else:
        xe, ye, de = ee(be, ae % be)
        return ye, xe - (ae // be) * ye, de


def inverse(ai, Ni):
    xi, yi, di = ee(ai, Ni)
    if di == 1:
        return xi % Ni
    else:
        return "none"


def is_prime(pp):
    if pp == 2:
        return 1
    elif pp % 2 == 0:
        return 0

    for a in range(3, 20):
        if exp(a, pp-1, pp) != 1 % pp:
            return False

        return True


# key p q: Print the modulus, public exponent, and private exponent of
# the RSA key pair derived from p and q. The public exponent must be the
# smallest positive integer that works; q must be positive and less than N.
def key(pk, qk):
    nk = pk * qk
    phi = (pk-1)*(qk-1)

    ek = 3
    # get lowest gcd
    while ek < phi:
        if gcd(ek, phi) == 1:
            break
        ek += 1

    dk = inverse(ek, phi)
    return nk, ek, dk


def main():
    while True:
        try:
            temp = input()

            if temp[0] is 'g':
                # GCD
                s = temp.split()
                a = int(s[1])
                b = int(s[2])
                g = gcd(a, b)
                print(g)
            elif temp[0] is 'e':
                # exp
                s = temp.split()
                x = int(s[1])
                y = int(s[2])
                N = int(s[3])
                print(exp(x, y, N))
            elif temp[0] is 'k':
                # key
                s = temp.split()
                p = int(s[1])
                q = int(s[2])
                N, e, d = key(p, q)
                print(N, e, d)
            elif temp[0] is 'i' and temp[1] is 's':
                # isprime
                s = temp.split()
                p = int(s[1])
                prime = is_prime(p)
                if prime is True:
                    print("yes")
                else:
                    print("no")
            elif temp[0] is 'i' and temp[1] is 'n':
                s = temp.split()
                # inverse
                a = int(s[1])
                N = int(s[2])
                print(inverse(a, N))

        except EOFError:
            break


if __name__ == "__main__":
    main()
