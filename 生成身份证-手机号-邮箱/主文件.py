import random
import logging
import pickle


logging.basicConfig(level=logging.INFO,format='%(levelname)s - %(asctime)s - %(message)s')

"""
TODO:
    1. 随机获取名字
    2. 随机获取性别 √
    3. 随机获取生日以及住址 √
    4. 随机获取身份证号 √
    5. 获取随机邮箱 √
    6. 检验身份证是否合法 X
"""
class FakeCn:
    
    def __init__(self):
        self.Sn = []
        self.idCard = ""
        self.email = ""
        self.phone = ""
        
        # 这个是官方检验码
        self.check = {'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'4','9':'3','10':'2'}
    
    def generateIdCard(self):
        # 默认生成一个身份证， 居住地址和生日都是随机
        
        # 根据公式，首先需要生成前6位的大地点
        with open('firstSixNumber.db','rb') as f:
            firstSixNumberList = pickle.load(f)
            firstSixNumber = random.choice(firstSixNumberList)
            self.idCard += firstSixNumber
        # 生成生日8位================================================================
        
        # 生成年份
        birYear = random.randint(1800,2022)
        self.idCard += str(birYear)
        
        # 生成月份
        birMonth = random.randint(1,12)
        if birMonth < 10:
            birMonth = '0' + str(birMonth)
        self.idCard += str(birMonth)
        
        # 生成日
        birDay = random.randint(1,30)
        if birDay < 10:
            birDay = '0' + str(birDay)
        self.idCard += str(birDay)
        
        # 2位的小地区
        smallArea = random.randint(10,99)
        self.idCard += str(smallArea)
        
        # 男女(男为奇数，女为偶数)
        gender = random.randint(1,9)
        self.idCard += str(gender)
        
        # 校验码生成====================================================      
        # 算出加权数
        for weighting in range(18,1,-1):            
            # 使用公式先算出Wi的值，Wi的值为加权数值的(2^(weighting-1)次方)%11
            Wi = (2**(weighting-1))%11
           
            # 使用加权的数字依次和身份证号的对应位相乘
            reverseIdCard = self.idCard[::-1]
                   
            s = int(reverseIdCard[weighting-2]) * Wi
            
            logging.debug(f'')
            logging.info(f'当前权重{weighting}\tWi = {Wi}\tAi = {reverseIdCard[weighting-2]}\ts = {s}')
               
            # 添加进总值内，等待最后做加法运算
            self.Sn.append(s)
        
        # 全部加起来后得出最后得数，然后除以11给出最后一位的值
        beforeCheck = str(sum(self.Sn) % 11)
        final = self.check[beforeCheck]
        self.idCard += str(final)
        
        return self.idCard
    
    def generateEmail(self):
        # 随机邮箱的长度，最短9位，最长11位
        mailLength = random.randint(9,11)
        # 随机邮箱的号码，第一位不能是0
        self.email += str(random.randint(1,6))
        
        for i in range(mailLength):
            self.email += str(random.randint(0,9))
        # 随机邮箱地址，目前有QQ,163,sina.com,sina.cn,yahoo.com,126.com,139.com
        emailType = ['@qq.com','@163.com','@sina.com','@sina.cn','@yahoo.com','@126.com','@139.com']
        
        # 拼接后返回
        fullEmail = self.email + random.choice(emailType)
        return fullEmail
        
    def generatePhone(self):
        # 随机选择运营商138,153,184
        supplier = ['138','153','184','178','152','158']
        self.phone += random.choice(supplier)
        # 随机生成剩下的8位数字
        for i in range(8):
            self.phone += str(random.randint(0,9))
        
        return self.phone
    
  
    def generateName(self):
        pass
    
    
            
    
a = FakeCn()
print(a.generatePhone())
#print(a.generateIdCard())