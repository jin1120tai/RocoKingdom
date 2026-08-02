def roco_evolution() :
    evo = {'039'            : '挖三次矿石' ,
           '矿晶虫'         : '挖三次矿石' ,
           'kuangjingchong' : '挖三次矿石' ,
           'kjc'            : '挖三次矿石' ,
           '060'            : '32级，击败3虫' ,
           '伏地兽'         : '32级，击败3虫' ,
           'fudishou'       : '32级，击败3虫' ,
           'fds'            : '32级，击败3虫' ,
           }

    while 1 :
        a = input('查阅进化方式请输入精灵昵称(三位编号/昵称全拼/昵称缩写):')
        if a in evo :
            print(evo[a])
            break
        else :
            print('输入错误，请重新输入')


while 1 :
    roco_evolution()
    mm = input('按任意键继续，仅按enter以结束')
    if mm == '' :
        print('---运行结束---')
        break
