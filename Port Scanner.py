import socket
from threading import *

def top1k(ip_address):
    thred = []
    for i in range(1,1001):
        t = Thread(target=scan, args=(ip_address,i))
        thred.append(t)
        t.start()

def all(ip_address):
    thred = []
    for i in range(1,65536):
        t = Thread(target=scan, args=(ip_address,i))
        thred.append(t)
        t.start()

def scan(ip_address,port):
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soc.settimeout(2)
    test = soc.connect_ex((ip_address,port))
    if test == 0:
        print("[+] Port: {}   Servis: {}   Versiyon: {}".format(port,service(ip_address,port),version(ip_address,port)))
    soc.close

def service(ip_address,port):
    soc =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soc.settimeout(2)
    soc.connect((ip_address,port))
    banner = socket.getservbyport(port)  
    return banner.upper()

def version(ip_address,port):
    try:
        if port == 80 or port == 443:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            soc.connect((ip_address,port))
            soc.send(b'GET HTTP/2.0 \r\n')
            banner = soc.recv(1024)
            soc.close()
            byte =banner.split(b"\n")
            last=byte[8].decode('UTF-8')
            return last[9:22]
        else:
            soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            soc.settimeout(2)
            soc.connect((ip_address,port))  
            banner = soc.recv(1024)
            soc.close()
            return banner.decode("UTF-8")
    except:
        pass

def main(sec,tara):
    if sec == "1":
        domain = input("Port Taraması İçin Domain Giriniz: ")
        if tara == "a" or tara == "A":
            top1k(socket.gethostbyname(domain))
        elif tara == "b" or tara == "B":
            all(socket.gethostbyname(domain))
    elif sec == "2":
        domain = input("Port Taraması İçin Ip Giriniz: ")
        if tara == "a" or tara == "A":
            top1k(domain)
        elif tara == "b" or tara == "B":
            all(domain)
        else:
            print("Geçersiz İşlem. Programdan Çıkılıyor...")
    else:
        print("Hatalı Bir Sayı Girdiniz. Programdan Çıkılıyor...")

print("""
İşlem Türü:

1-) Domain Scan
    a-) İlk 1000(Bin) Port
    b-) Tüm Portlar
2-) Ip Scan
    a-) İlk 1000(Bin) Port
    b-) Tüm Portlar

    """)
select = input("Lütfen Yukarıdaki Seçeneklerden Birinin Numarasını Giriniz(1/2): ")
tara = input("Lütfen Listede Görünen Port Tarama Türlerinden Birini Giriniz(a/b):")
main(select,tara)
