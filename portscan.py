import socket, os, sys, threading
minD = 1 #min port
maxD = 10000 #max port
hostname = "localhost"
timeout = 6 #timeout for connection
thrcount = 0 #output threads counter
ver = '1.0' 
ports = [] 
PRC = 0 
def bubblesort(a):
    for _ in range(len(a)):
        for i in range(len(a)):
            try:
                if a[i] > a[i+1]:
                    b = a[i]
                    a[i] = a[i+1]
                    a[i+1] = b
            except:
                continue
    return a
def addP(): 
    global PRC
    PRC+=1
def perc(num, maxn, minn): 
    return ((num - minn) / ((maxn - minn)/100))
def tryPort(ip, port): 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.settimeout(timeout) 
    try: 
        s.connect((ip, port)) 
        ports.append(port) 
        return 1
    except:
        return 0 
def Scan(host, minD, maxD): 
    global ports
    ports = []
    
    ip = socket.gethostbyname(host)
    thrds = []
    for port in range(maxD):
        math = threading.Thread(target = tryPort, args = (ip, port+minD))
        thrds.append(math) 
    for i in range(maxD):
        thrds[i].start()
        prc = int(perc(i+1, maxD, minD)) 
        Prc = PRC
        if prc > Prc:
            if thrcount == 1:
                print("Scanning ", prc, "% Threads: ", i, end='\r')
            else:
                print("Scanning ", prc, "%", end = '\r') 
            addP()
    ports = bubblesort(ports)
    print(' '*54, end = '\r')
    print("="*16)
    print("Host: "+hostname) 
    print("IP: "+ip)
    print("="*16)
    for i in range(len(ports)):
        print(ports[i], " is open!      ")
    print("="*16)
def main(): 
    global hostname 
    hostname = input("Host >> ") 
    ip = socket.gethostbyname(hostname) 
    Scan(ip, minD, maxD) 
    os.system("pause")
main()