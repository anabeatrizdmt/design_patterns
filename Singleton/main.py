class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s1 = Singleton()
print(s1)

s2 = Singleton.getInstance()
print(s2)

s3 = Singleton.getInstance()
print(s3)
