# encoding : utf-8
from socket import *

PORT = 5050

def main():
    a = ["0","0","0","0","0","0","0"]
    while True:

        menuswitch = input("수정화면으로 가려면 E키 : ")

        if (menuswitch == "e" or menuswitch == "E"):
            while True:
                getnum = input('1.수분상태/2.부동액/3.밧데리/4.엔진수온/5.엔진오일/6.미션오일/7.안전상태, 나가려면 Q키')
                if(getnum=="Q" or getnum == "q"):
                    break
                if(int(getnum)>7 and int(getnum)<1):
                    continue
                getstat = input('해당 타입의 상태 입력')
                a[int(getnum)-1] = getstat
                continue

        client = socket(AF_INET, SOCK_DGRAM)
        parse = "/"
        str = ""
        for i in range(len(a)):
            str += a[i]
            str += parse
        sentence = (str).encode('utf-8')
        print(sentence)
        client.sendto(sentence,('127.0.0.1', PORT))

if __name__ == '__main__':
    main()