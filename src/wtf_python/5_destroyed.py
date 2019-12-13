class WTF:
    pass


WTF() == WTF()  # two different instances can't be equal
# ?

WTF() is WTF()  # identities are also different
# ?

hash(WTF()) == hash(WTF()) # hashes _should_ be different as well
# ?

id(WTF()) == id(WTF())
# ?


class WTF(object):
    def __init__(self):
        print("I")
    def __del__(self):
        print("D")


WTF() is WTF()
id(WTF()) == id(WTF())
