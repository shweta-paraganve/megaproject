import sys
import subprocess
import requests
import webbrowser
import os 
cwd = os.getcwd()
def extracterror(cmd):
    
    
    cmptime = subprocess.call(["g++", "error.cpp"]) # OR gcc for c program
    if(cmptime==0):
        runtime = subprocess.call("./a.out")
        if(runtime==0):
            print("No errors found!")
        else:
            print("runtime error")
            tmp = subprocess.Popen("./a.out",stdout=subprocess.PIPE,stderr = subprocess.PIPE)
            out= tmp.stderr.read().decode("utf-8")
            print("out")
            print(out)
    else:
        print("compile-time error")
        cmp= subprocess.Popen(["g++", "error.cpp"],stdout=subprocess.PIPE,stderr = subprocess.PIPE)
        out= cmp.stderr.read().decode("utf-8")
    
    out.rstrip('\n')
    stroutput = (out.splitlines())
    errormsg = ""
    errortype =""
    for line in stroutput:
        if "error:" in line:
            errortype,errormsg = line.split('error:')
            c=1
            break
    
    print(errormsg)
    sendreq(errormsg)


        
        
def getlinks(rjson):     
    url_list = []
    countlinks=0
        
    for i in rjson["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
        countlinks+=1
        if(countlinks==5 or countlinks==len(rjson["items"])):
            break
        
    for i in url_list:
        webbrowser.open(i)

def sendreq(stroutput):
    errortype,errormsg = stroutput.split('Error:')
    respoutput = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(stroutput))
    restype = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errortype))
    respmsg = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errormsg))
    getlinks(respoutput.json())
    getlinks(restype.json())
    getlinks(respmsg.json())

if __name__ == "__main__":
    extracterror("error.cpp")



