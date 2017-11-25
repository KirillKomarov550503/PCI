import os
import subprocess

class ID:
    def __init__(self):
        subprocess.call("lspci -mmnn > " + os.getcwd() + "/temp.txt", shell=True)
        self.keys = ["vendorID", "deviceID"]

    def OpenFile(self):
        self.log = open(os.getcwd() + "/temp.txt")
        print("self.log: ", self.log)

    def Parse(self):
        for i in self.log:
            lst = i.split(" \"")
            if(len(lst) > 1):
                dictionary = {self.keys[j]: (lst[j + 2][0: -1]) for j in range(0, len(self.keys))}
                listDev = dictionary["deviceID"]
                tempList = listDev.split("\"")
                dictionary["deviceID"] = tempList[0]
                print(dictionary)

    def RemoveFile(self):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.getcwd() + "/temp.txt")
        os.remove(path)


    def CloseFile(self):
        self.log.close()

if __name__ == "__main__":
    obj = ID()
    obj.OpenFile()
    obj.Parse()
    obj.CloseFile()
    obj.RemoveFile()
