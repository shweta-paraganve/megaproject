
import requests
import webbrowser

import sys
import subprocess

def extracterror(cmd):
    
    theproc = subprocess.Popen([sys.executable, cmd],stdout=subprocess.PIPE,stderr = subprocess.PIPE)
    out = theproc.stderr.read().decode("utf-8") 
    out.rstrip('\n')
    
    if(out):
        stroutput = (out.splitlines()[-1])
        print(stroutput)
        sendreq(stroutput)
        
    else:
        print("No errors found!")
        
        
import webbrowser
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

import requests

def sendreq(stroutput):
    errortype,errormsg = stroutput.split('Error:')
    respoutput = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(stroutput))
    restype = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errortype))
    respmsg = requests.get("https://api.stackexchange.com/"+"/2.2/search?order=desc&sort=activity&tagged=Python&intitle={}&site=stackoverflow".format(errormsg))
    print(respmsg.json())
    getlinks(respoutput.json())
    getlinks(restype.json())
    getlinks(respmsg.json())

if __name__ == "__main__":
    extracterror("error.py")



