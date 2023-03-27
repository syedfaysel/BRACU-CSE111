# class Test4:
#     def __init__(self):
#         self.sum, self.y = 0, 0

#     def methodA(self):
#         x, y = 0, 0
#         msg = [0]
#         msg[0] = 5
#         y = y + self.methodB(msg[0])
#         x = y + self.methodB(msg, msg[0])
#         self.sum = x + y + msg[0]
#         print(x, y, self.sum)

#     def methodB(self, *args):
#         if len(args) == 1:
#             mg1 = args[0]
#             x, y = 0, 0
#             y = y + mg1
#             x = x + 33 + mg1
#             self.sum = self.sum + x + y
#             self.y = mg1 + x + 2
#             print(x, y, self.sum)
#             return y
#         else:
#             mg2, mg1 = args
#             x = 0
#             self.y = self.y + mg2[0]
#             x = x + 33 + mg1
#             self.sum = self.sum + x + self.y
#             mg2[0] = self.y + mg1
#             mg1 = mg1 + x + 2
#             print(x, self.y, self.sum)
#             return self.sum


# t3 = Test4()
# t3.methodA()
# t3.methodA()
# t3.methodA()
# t3.methodA()





# Task 19 : For Tracing

class msgClass:
    def __init__(self):
        self.content = 0 
class Q5:
    def __init__(self):
        self.sum = 1
        self.x = 2
        self.y = 3 
    def methodA(self):
        x, y = 1, 1
        msg = []


        myMsg = msgClass()
        myMsg.content = self.x
        msg.append(myMsg)
        msg[0].content = self.y + myMsg.content
        self.y = self.y + self.methodB(msg[0])
        y = self.methodB(msg[0]) + self.y
        # custom
        print(self.y)
        x = y + self.methodB(msg[0], msg)
        self.sum = x + y + msg[0].content
        print(x," ", y," ", self.sum)    
    def methodB(self, mg1, mg2 = None):
        if mg2 == None:
            x, y = 5, 6
            y = self.sum + mg1.content
            self.y = y + mg1.content
            x = self.x + 7 +mg1.content
            self.sum = self.sum + x + y
            self.x = mg1.content + x +8
            print(x, " ", y," ", self.sum)
            return y
        else:
            x = 1
            self.y += mg2[0].content
            mg2[0].content = self.y + mg1.content
            x = x + 4 + mg1.content
            self.sum += x + self.y
            mg1.content = self.sum - mg2[0].content
            print(self.x, " ",self.y," ", self.sum)
            return self.sum
# here is the breakpoint
q = Q5()
q.methodA()
