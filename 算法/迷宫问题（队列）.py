from collections import deque

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

def show_path(path):

    real_path = []
    lastNode = path[-1]

    while lastNode[2] != -1:

        real_path.append(lastNode[0:2])
        lastNode = path[lastNode[2]]

    real_path.append(path[0][:2])
    real_path.reverse()
    for each in real_path:
        print(each)
    for each in range(1, len(real_path)):
        curNode = real_path[each - 1]
        nextNode = real_path[each]
        if curNode[0] - nextNode[0] < 0:
            print('↓\t', end='')
        elif curNode[0] - nextNode[0] > 0:
            print('↑\t', end='')
        elif curNode[1] - nextNode[1] < 0:
            print('→\t', end='')
        elif curNode[1] - nextNode[1] > 0:
            print('←\t', end='')



def maze_path(x1, y1, x2, y2):
    moveable = [
        lambda x, y:(x, y+1),
        lambda x, y:(x+1, y),
        lambda x, y:(x, y-1),
        lambda x, y:(x-1, y)
    ]

    queue = deque()

    # 创建起始点
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print('找到了一条路')
            show_path(path)
            return True

        for next_one in moveable:
            nextNode = next_one(curNode[0], curNode[1])

            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                # 标记已经走过
                maze[curNode[0]][curNode[1]] = 2
    else:
        print('没有找到路')
        return False


maze_path(1, 1, 3, 8)
