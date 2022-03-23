'''
轮子功能:
    输入一段字符串，比较他和另一对字符串的匹配度并返回
    4个参数
    orgin = 表示需要获得匹配度的字
    target = 表示目标
    mode == 1 时表示强制匹配
    mode == 2 时表示模糊匹配(在这个模式下orgin和target的顺序不再重要)
    search 表示强制模式下是否从头开始匹配(0表示从头开始匹配,1表示从需要匹配的第一个字符串开始匹配),该项默认值为0
'''
def compare(orgin,target,mode = 2,search = 0):
    
    #mode = 1是强制匹配
    correct = worry = 0
    if mode == 1:
        #一个是分母一个是分子 
        if search == 1:
            start_position = target.find(orgin[0])
            print(start_position)
            target = target[start_position:]
        for number in range(len(orgin)):
            if orgin[number] == target[number]:
                correct += 1
        return round(correct/len(target),3)
    
    #mode = 2是模糊匹配
    elif mode == 2:
        modify_target = target
        for each in orgin:
            #若果检测到一样的就删了
            if each in modify_target:
                #删去一个字符
                
                modify_target = modify_target.replace(each,'',1)
                correct += 1
            else:
                worry += 1
                
        print(f'一共有[{worry}]处不同')
        return round(correct/(len(target) + worry),3)
if __name__ == '__main__':
    print(compare('13','4135',mode = 2,search = 1))