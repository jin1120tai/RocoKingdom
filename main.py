from RocoAttribute import roco_attribute_
from RocoEvolution import roco_evolution_

while 1 :
    c = input('1.属性克制查询  2.特殊进化查询  (enter结束):')
    if c == '1' :
        roco_attribute_()
    elif c == '2' :
        roco_evolution_()
    elif c == '' :
        print('---运行结束---')
        break
