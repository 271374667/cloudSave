import easygui as g
import os
import os.path
import shutil as sl
from tqdm import tqdm


class CopyFile:
    def __init__(self):
        # 创建一个计数器，作为区分id,防止文件名重复
        self.counter = 0
        
        self.ext = g.enterbox(msg="请输入后缀\n格式.txt\t.jpg",title="请输入后缀名",default=".txt")
        # 需要指定一个目录
        self.inPutDir = g.diropenbox(msg="请选择一个文件夹作为起始目录")
        self.outPutDir = g.diropenbox(msg="请选择一个文件夹作为导出目录")
        

    # 定义一个函数，遍历目录下所有的文件夹，反复调用，直到最终文件夹内没有额外的文件夹
    def findAllFiles(self):
        allFileList = []
        for root, dirs, files in os.walk(self.inPutDir):
            for file in files:
                # 在文件夹下面使用if判断是否后缀相同
                if self.ext in file:
                    allFileList.append(os.path.join(root, file))
                    #print(allFileList[-1])
        return allFileList

    def moveToOutputDir(self):
        allPathList = self.findAllFiles()
        with tqdm(total=len(allPathList),ncols=100,desc="正在进行移动文件") as bar:      
            for eachPath in allPathList:
                bar.set_description(f'正在移动{str(eachPath[-10:])}')
                bar.update(1)
                sl.copy(eachPath, self.outPutDir+"/"+str(self.counter) + self.ext)
                self.counter += 1


# 移动这些符合规则的文件进入预定要移入的文件夹
a = CopyFile()
a.moveToOutputDir()
