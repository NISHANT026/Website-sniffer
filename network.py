import pandas as pd
dict = {}
web={
 "182.79.130.13":"Bharti Airtel",
 "182.79.148.16":"Bharti Airtel",
 "172.217.163.174":"Google",
 "103.37.200.180":"Channel i",
 "216.58.197.35":"Youtube",
 "172.217.166.86":"Google"
}
def parseCSV():
    df = pd.read_csv("go.csv")
    saved_column = df.Destination
    for i in saved_column:
        if not i in dict:
            dict[i]=1
            
        else:
            dict[i]+=1

def isIPv4(s):
    try: return str(int(s)) == s and 0 <= int(s) <= 255
    except: return False
def valid(IP):
    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
         return True            
def printTop3():
    print("Top 3 IP")
    Keymax = max(dict, key=dict.get)
    del dict[Keymax]
    count=0
    while(count<4):
        Keymax = max(dict, key=dict.get)
        if valid(Keymax):
            print(web[Keymax],Keymax,dict[Keymax])
            #print(Keymax,dict[Keymax])
            count+=1
        del dict[Keymax]             
#print(saved_column)

def main():
    parseCSV()
    #print(dict)
    printTop3()

main()