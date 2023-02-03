from collections import defaultdict
import math
addset=[]
strength=defaultdict(lambda: 5)
def add_func(in2,in3):
    if(in2=="COMPUTER" or in2=="REPEATER"):
        if([in2,in3] not in addset):
            addset.append([in2,in3])
            return "Successfully added "+str(in3)+"."
        else:
            return "Error: That name already exists."
    else:
        return "Error: Invalid command syntax."

def set_device_strength(in2,in3):
    if not (in3.isnumeric()):
        return "Error: Invalid command syntax."
    else:
        if int(in3)<0:return "Error: Invalid command syntax."
        else:
            strength[in2]=in3
            return "Successfully defined strength."

def connect_func(self):
    return 0
def info_route(self):
    return 0

def main():
    a=input()
    try:
        # just=list(map(str,a.split()))
        # if(len(just)==3):
        #     in1=just[0]
        #     in2=just[1]
        #     in3=just[2]
        # elif(len(just)>1):
        #     in1=just[0]
        #     if in1=="SET_DEVICE_STRENGTH":
        #         if(len(just)==2):
        #             in3=5
        #     else:
        #         print("Error: Invalid command syntax.")
        # else:
        #     print("Error: Invalid command syntax.")
        in1, in2, in3 = list(map(str, a.split()))
    except:
        if in1=="SET_DEVICE_STRENGTH":
            if not(in2):
                print("Error: Invalid command syntax.")

            elif in3:
                in3=in3
            else:
                in3=5
        else:
            print("Error: Invalid command syntax.")
        main()


    if(in1 == "ADD"):
        print(add_func(in2,in3))
        main()
    elif(in1=="CONNECT"):
        print(connect_func())
        main()
    elif(in1=="INFO_ROUTE"):
        print(info_route())
        main()
    elif(in1=="SET_DEVICE_STRENGTH"):
        print(set_device_strength(in2,in3))
        main()

main()
