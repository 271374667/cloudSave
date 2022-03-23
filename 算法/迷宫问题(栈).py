maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# x1,y1,x2,y2分别是起点坐标和终点坐标


def maze_path(x1, y1, x2, y2):
    pathNode = []
    pathNode.append((x1, y1))
    # 当栈不为空的时候不断循环

    moveable = [
        lambda x, y:(x, y+1),
        lambda x, y:(x+1, y),
        lambda x, y:(x, y-1),
        lambda x, y:(x-1, y)
    ]

    while pathNode != []:
        currentNode = pathNode[-1]
        
        #如果找到了路径
        if currentNode[0] == x2 and currentNode[1] == y2:
            #打印一下路径
            for each in pathNode:
                print(each)
            return True


        for dir in moveable:
            next_node = dir(currentNode[0],currentNode[1])
        
            if maze[next_node[0]][next_node[1]] == 0:
                # 表示有路可以走
                pathNode.append(next_node)
                # 走完以后标记一下，防止之后再走
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            #表示无路可走，开始回退
            pathNode.pop()
    else:
        print('没有通往终点的路')
        return False

maze_path(1,1,3,5)
