
class Singleton:
    
    __instance = False
    
    def __new__(self):
        if not self.__instance:
            self.__instance = object.__new__(self)
        return self.__instance
    
    def __init__(self):
       pass

# main method
if __name__ == "__main__":

    # create object of Singleton Class
    obj = Singleton()
    print(obj)

    # pick the instance of the class
    obj = Singleton()
    
    print(obj == Singleton())
    print(obj)
