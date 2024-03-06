import logging
values = [10,0,6,1]
for value in values:
    try:
        pass
        #print(100/value)
    except ZeroDivisionError:
        pass
        #print("1")

    except Exception as e:
        pass
        #logging.exception(e)
    else:
        pass
        #print("i dont care")#no exception
#print("end")

class myClass:
    def doSomething(self,x,y):
        try:
            print(x/y)
        except ZeroDivisionError:
            print("hello there was exception")
mc=myClass()
mc.doSomething(1,1)