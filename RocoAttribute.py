def roco_attribute_() :
    z_to_w = {
        0  : "普通" ,
        1  : "草" ,
        2  : "火" ,
        3  : "水" ,
        4  : "光" ,
        5  : "地" ,
        6  : "冰" ,
        7  : "龙" ,
        8  : "电" ,
        9  : "毒" ,
        10 : "虫" ,
        11 : "武" ,
        12 : "翼" ,
        13 : "萌" ,
        14 : "幽" ,
        15 : "恶" ,
        16 : "机械" ,
        17 : "幻" ,
        18 : 'None' ,
    }
    w_to_z = {'普通'  : 0 ,
              '草'    : 1 ,
              '火'    : 2 ,
              '水'    : 3 ,
              '光'    : 4 ,
              '地'    : 5 ,
              '冰'    : 6 ,
              '龙'    : 7 ,
              '电'    : 8 ,
              '毒'    : 9 ,
              '虫'    : 10 ,
              '武'    : 11 ,
              '翼'    : 12 ,
              '萌'    : 13 ,
              '幽'    : 14 ,
              '恶'    : 15 ,
              '机械'  : 16 ,
              '幻'    : 17 ,
              'p'     : 0 ,
              'pt'    : 0 ,
              'c'     : 1 ,
              'cao'   : 1 ,
              'h'     : 2 ,
              'huo'   : 2 ,
              's'     : 3 ,
              'shui'  : 3 ,
              'g'     : 4 ,
              'guang' : 4 ,
              'd'     : 5 ,
              'di'    : 5 ,
              'b'     : 6 ,
              'bing'  : 6 ,
              'l'     : 7 ,
              'long'  : 7 ,
              'dian'  : 8 ,
              'da'    : 8 ,
              'du'    : 9 ,
              'ch'    : 10 ,
              'chong' : 10 ,
              'w'     : 11 ,
              'wu'    : 11 ,
              'E'     : 12 ,
              'y'     : 12 ,
              'yi'    : 12 ,
              'f'     : 12 ,
              'm'     : 13 ,
              'meng'  : 13 ,
              'yo'    : 14 ,
              'you'   : 14 ,
              'u'     : 14 ,
              'e'     : 15 ,
              'j'     : 16 ,
              'jx'    : 16 ,
              'ha'    : 17 ,
              'huan'  : 17
              }

    def kz(s) :
        kz_a = []
        if s == 0 :
            kz_a = [18]
        elif s == 1 :
            kz_a = [3 , 4 , 5]
        elif s == 2 :
            kz_a = [1 , 6 , 10 , 16]
        elif s == 3 :
            kz_a = [2 , 5 , 16]
        elif s == 4 :
            kz_a = [14 , 15]
        elif s == 5 :
            kz_a = [2 , 6 , 8 , 9]
        elif s == 6 :
            kz_a = [1 , 5 , 7 , 12]
        elif s == 7 :
            kz_a = [7]
        elif s == 8 :
            kz_a = [3 , 12]
        elif s == 9 :
            kz_a = [1 , 13]
        elif s == 10 :
            kz_a = [1 , 15 , 17]
        elif s == 11 :
            kz_a = [0 , 5 , 6 , 15 , 16]
        elif s == 12 :
            kz_a = [1 , 10 , 11]
        elif s == 13 :
            kz_a = [7 , 11 , 15]
        elif s == 14 :
            kz_a = [4 , 14 , 17]
        elif s == 15 :
            kz_a = [9 , 13 , 14]
        elif s == 16 :
            kz_a = [5 , 6 , 13]
        elif s == 17 :
            kz_a = [9 , 11]

        return kz_a

    def bdk(s) :
        bdk_a = []
        if s == 0 :
            bdk_a = [5 , 14 , 16]
        elif s == 1 :
            bdk_a = [2 , 7 , 9 , 10 , 12 , 16]
        elif s == 2 :
            bdk_a = [3 , 5 , 7]
        elif s == 3 :
            bdk_a = [1 , 6 , 7]
        elif s == 4 :
            bdk_a = [1 , 6]
        elif s == 5 :
            bdk_a = [1 , 11]
        elif s == 6 :
            bdk_a = [2 , 6 , 16]
        elif s == 7 :
            bdk_a = [16]
        elif s == 8 :
            bdk_a = [1 , 5 , 7 , 8]
        elif s == 9 :
            bdk_a = [5 , 9 , 14 , 16]
        elif s == 10 :
            bdk_a = [2 , 9 , 11 , 12 , 13 , 14 , 16]
        elif s == 11 :
            bdk_a = [9 , 10 , 12 , 13 , 14 , 17]
        elif s == 12 :
            bdk_a = [5 , 7 , 8 , 16]
        elif s == 13 :
            bdk_a = [2 , 9 , 16]
        elif s == 14 :
            bdk_a = [0 , 15]
        elif s == 15 :
            bdk_a = [4 , 11 , 15]
        elif s == 16 :
            bdk_a = [2 , 3 , 8 , 16]
        elif s == 17 :
            bdk_a = [4 , 16 , 17]

        return bdk_a

    def bkz(s) :
        bkz_a = []
        if s == 0 :
            bkz_a = [11]
        elif s == 1 :
            bkz_a = [2 , 6 , 9 , 10 , 12]
        elif s == 2 :
            bkz_a = [3 , 5]
        elif s == 3 :
            bkz_a = [1 , 8]
        elif s == 4 :
            bkz_a = [1 , 14]
        elif s == 5 :
            bkz_a = [1 , 3 , 6 , 11 , 16]
        elif s == 6 :
            bkz_a = [2 , 5 , 11 , 16]
        elif s == 7 :
            bkz_a = [6 , 7 , 13]
        elif s == 8 :
            bkz_a = [5]
        elif s == 9 :
            bkz_a = [5 , 15 , 17]
        elif s == 10 :
            bkz_a = [2 , 12]
        elif s == 11 :
            bkz_a = [12 , 13 , 17]
        elif s == 12 :
            bkz_a = [6 , 8]
        elif s == 13 :
            bkz_a = [9 , 15 , 16]
        elif s == 14 :
            bkz_a = [4 , 14 , 15]
        elif s == 15 :
            bkz_a = [4 , 10 , 11 , 13]
        elif s == 16 :
            bkz_a = [2 , 3 , 11]
        elif s == 17 :
            bkz_a = [10 , 14]

        return bkz_a

    def dk(s) :
        dk_a = []
        if s == 0 :
            dk_a = [14]
        elif s == 1 :
            dk_a = [3 , 4 , 5 , 8]
        elif s == 2 :
            dk_a = [1 , 6 , 10 , 13 , 16]
        elif s == 3 :
            dk_a = [2 , 16]
        elif s == 4 :
            dk_a = [15 , 17]
        elif s == 5 :
            dk_a = [0 , 2 , 8 , 9 , 12]
        elif s == 6 :
            dk_a = [3 , 4 , 6]
        elif s == 7 :
            dk_a = [1 , 2 , 3 , 8 , 12]
        elif s == 8 :
            dk_a = [8 , 12 , 16]
        elif s == 9 :
            dk_a = [1 , 9 , 10 , 11 , 13]
        elif s == 10 :
            dk_a = [1 , 11]
        elif s == 11 :
            dk_a = [5 , 10 , 15]
        elif s == 12 :
            dk_a = [1 , 10 , 11]
        elif s == 13 :
            dk_a = [10 , 11]
        elif s == 14 :
            dk_a = [0 , 9 , 10 , 11]
        elif s == 15 :
            dk_a = [14 , 15]
        elif s == 16 :
            dk_a = [0 , 1 , 6 , 7 , 9 , 10 , 12 , 13 , 16 , 17]
        elif s == 17 :
            dk_a = [11 , 17]

        return dk_a

    # 显示宽度（中文/全角符号算 2），用于输出对齐
    def _w(s) :
        w = 0
        for c in s :
            w += 2 if ord(c) > 127 else 1
        return w

    # 把 s 用空格填充到指定显示宽度
    def _pad(s , n) :
        return s + ' ' * (n - _w(s))

    while 1 :
        s_main , s_other , *_ = (input("请输入属性：").split() + [""])[:2]

        out_ = {'a' , 'i' , 'k' , 'n' , 'o' , 'r' , 't' , 'v' , 'x' , 'z'}
        if (s_main in out_) or (s_other in out_) :
            print('输入错误，你不应该输入以下内容：\n' , out_ , '\n请重新输入')
        else :
            break
    str1 = ''

    if s_other == '' :

        str1 += _pad('正在搜索：' , 10) + '【' + z_to_w[w_to_z[s_main]] + '】\n'

        d_kz = kz(w_to_z[s_main])
        d_bdk = bdk(w_to_z[s_main])
        d_bkz = bkz(w_to_z[s_main])
        d_dk = dk(w_to_z[s_main])

        str1 += _pad('克  制：' , 10) + ' '.join(z_to_w[i] for i in d_kz) + '\n'
        str1 += _pad('被抵抗：' , 10) + ' '.join(z_to_w[i] for i in d_bdk) + '\n'
        str1 += _pad('被克制：' , 10) + ' '.join(z_to_w[i] for i in d_bkz) + '\n'
        str1 += _pad('抵  抗：' , 10) + ' '.join(z_to_w[i] for i in d_dk)

    else :

        nm = '【' + z_to_w[w_to_z[s_main]] + '】'
        no = '【' + z_to_w[w_to_z[s_other]] + '】'

        d_kz1 = kz(w_to_z[s_main])
        d_bdk1 = bdk(w_to_z[s_main])
        d_bkz1 = bkz(w_to_z[s_main])
        d_dk1 = dk(w_to_z[s_main])

        d_kz2 = kz(w_to_z[s_other])
        d_bdk2 = bdk(w_to_z[s_other])
        d_bkz2 = bkz(w_to_z[s_other])
        d_dk2 = dk(w_to_z[s_other])

        # 两列行（克制/被抵抗）第一列内容，取最大宽度对齐第二列
        b_kz = ' '.join(z_to_w[i] for i in d_kz1)
        b_bdk = ' '.join(z_to_w[i] for i in d_bdk1)
        bw = max(_w(nm) , _w(b_kz) , _w(b_bdk)) + 2

        str1 += _pad('正在搜索：' , 10) + _pad(nm , bw) + no + '\n'
        str1 += _pad('克  制：' , 10) + _pad(b_kz , bw) + ' '.join(z_to_w[i] for i in d_kz2) + '\n'
        str1 += _pad('被抵抗：' , 10) + _pad(b_bdk , bw) + ' '.join(z_to_w[i] for i in d_bdk2) + '\n'

        del_ = ((set(bkz(w_to_z[s_main])) & set(dk(w_to_z[s_other])))
                | (set(dk(w_to_z[s_main])) & set(bkz(w_to_z[s_other]))))

        do_bkz = sorted(list((set(d_bkz1) | set(d_bkz2)) - del_))
        de_bkz = sorted(list(set(d_bkz1) & set(d_bkz2)))
        s_bkz = ' '.join(z_to_w[i] for i in de_bkz)
        if de_bkz :
            s_bkz += ' <- '
        s_bkz += ' '.join(z_to_w[i] for i in do_bkz)
        str1 += _pad('被克制：' , 10) + s_bkz + '\n'

        do_dk = sorted(list((set(d_dk1) | set(d_dk2)) - del_))
        de_dk = sorted(list(set(d_dk1) & set(d_dk2)))
        s_dk = ' '.join(z_to_w[i] for i in de_dk)
        if de_dk :
            s_dk += ' <- '
        s_dk += ' '.join(z_to_w[i] for i in do_dk)
        str1 += _pad('抵  抗：' , 10) + s_dk

    print(str1)
