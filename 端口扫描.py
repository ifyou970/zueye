import socket
#循环
while True:
    #引入协议族AF_INET和SOCK_STREAM
    sm=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sm.settimeout(1)
    ip = input("请输入靶机ip：")
    dk=input("请输入目标靶机开始端口:")
    startport = int(dk)
    dk= input("请输入目标靶机结束端口：")
    endport = int(dk)

    for port in range(startport, endport + 1):
        print("正在扫描端口：%d" % port)
        try:
            sm.connect((ip, port))
            print("服务器 %s 端口 %d 开启!" % (ip, port))
        except Exception:
            print("服务器 %s 端口 %d 找不到!" % (ip, port))
    sm.close()
