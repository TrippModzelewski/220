def encode(x, k):
    acc = ""
    for i in range(len(x)):
        n = ord(x[i])
        s = n + k
        secret_character = chr(s)
        acc = acc + secret_character
    return acc


def encode_better(m, k):
    acc = ""
    for i in range(len(m)):
        mi = ord(m[i])
        ki = ord(k[i % len(k)]) - 97
        result = mi + ki
        acc = acc + chr(result)
    return acc
