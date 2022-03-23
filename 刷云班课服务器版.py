import requests
import json
import logging
import datetime
from bs4 import BeautifulSoup
logging.basicConfig(level=logging.INFO,
                    format=f'%(levelname)s - %(asctime)s - %(message)s')


class Cloud_class:
    try:
        def __init__(self,account,password):

            self.all_class_id = []
            self.account = account

            self.url = 'https://coreapi-proxy.mosoteach.cn/index.php/passports/account-login'
            self.headers = {
                'Referer': 'https://www.mosoteach.cn/',
                'Connection': 'keep-alive',
                'Host': 'coreapi-proxy.mosoteach.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
            }

            data = {"account": account, "password": password}
            data = json.dumps(data)

            logging.info('starting')
            self.session = requests.Session()
            response = self.session.post(
                url=self.url, data=data, headers=self.headers)

            infos_return = json.loads(response.text)
            logging.debug(infos_return)
            self.token = infos_return['token']

            response = self.session.get(url=f'https://www.mosoteach.cn/web/index.php?c=passport&m=save_proxy_token&proxy_token={self.token}&remember_me=N', headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
            })
            self.home_login()

        def home_login(self):
            # 进入登录后的主页
            home_url = 'https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=my_joined'

            header = {
                'Referer': 'https://www.mosoteach.cn/web/index.php?c=clazzcourse&m=index',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
            }

            response = self.session.post(url=home_url, headers=header)
            response = json.loads(response.text)
            # 获取所有科目的id
            for i in response['data']:
                self.all_class_id.append((i.get('id'), i["course"].get('name')))

            logging.debug(self.all_class_id)

        def run(self):

            for each_class, class_name in self.all_class_id:
                logging.info(f'当前正在刷取:{class_name},科目ID编号为:{each_class}')
                headers = {
                    'Referer': f'https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={each_class}',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
                }
                url = f'https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={each_class}'
                response = self.session.get(url=url, headers=headers)
                logging.debug(response.text)

                soup = BeautifulSoup(response.text, 'lxml')
                infos = soup.select(
                    '#res-list-box > div > div[class = "hide-div"] > div')

                # 每个作业开始刷
                for each in infos:

                    # 筛掉那些刷过的文件color:#ec6941表示没刷过
                    if each.select('span[style = "color:#ec6941"]') == []:
                        continue

                    name = each.select(
                        'div[class="res-info"]  span[class="res-name"] ')[0]['title']
                    data_mine = each['data-mime']
                    data_value = each['data-value']
                    # operater_id = each['operater_id']
                    logging.info(f'当前正在执行：{name}')

                    # 进行特殊格式处理
                    if data_mine == 'video':
                        # continue
                        headers = {'Referer': f'https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={each_class}',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                                'Host': 'www.mosoteach.cn',
                                'X-Requested-With': 'XMLHttpRequest',
                                'Content-Encoding': 'gzip',
                                'Content-Type': 'application/json; charset=utf-8',
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                                }

                        # 模拟点开视频
                        data = {
                            'file_id': data_value,
                            'type': 'VIEW',
                            'clazz_course_id': each_class
                        }
                        url = 'https://www.mosoteach.cn/web/index.php?c=res&m=request_url_for_json'
                        response = self.session.post(
                            url, headers=headers, data=data)
                        logging.debug(response.text)

                        # 获取video的信息
                        url = 'https://www.mosoteach.cn/web/index.php?c=res&m=get_video_record'
                        data = {'res_id': data_value}
                        #data = json.dumps(data)
                        response = self.session.post(
                            url=url, headers=headers, data=data)
                        infos_return = json.loads(response.text)
                        logging.debug(response.text)

                        url = 'https://www.mosoteach.cn/web/index.php?c=res&m=save_watch_to'

                        data = {
                            'clazz_course_id': each_class,
                            'res_id': data_value,
                            'watch_to': '100000',
                            'duration': '100000',
                            'Referer': f'https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id={each_class}',
                            'Host': 'www.mosoteach.cn'
                        }
                        #data = json.dumps(data)
                        response = self.session.post(
                            url=url, headers=headers, data=data)
                        logging.debug(response.text)
                        if response.text == '["success"]':
                            logging.info(f'成功刷了一个视频{name}')
                        else:
                            logging.info(f'当前视频{name},刷视频失败:{response.text}')

                    # 其他模式直接打开就完事
                    else:
                        logging.info(
                            f'当前文件{name}的格式是{data_mine},启动浏览模式,正在浏览ing!!!')
                        headers = {
                            'referer': 'https://www.mosoteach.cn/',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
                        }
                        body = {}
                        url = f'https://www.mosoteach.cn/web/index.php?c=res&m=download&file_id={data_value}&clazz_course_id={each_class}'
                        try:
                            response = self.session.post(
                                url=url, headers=headers, json=body, timeout=0.2)
                            logging.debug(response.text)

                        except Exception as e:
                            logging.info(f'#####完成浏览一个文件{name}#####')

                else:
                    logging.info(f'当前:{class_name}已经干净的很啦，全部都被刷了一遍！！！\n\n')
                    # logging.info(f'{name}')
                # break
    except Exception as e:
        notifyTime = str(datetime.datetime.now())
        msg = f'当前出现了致命错误:' + '\n\n' + '出现错误的时间：' + '\n\n' + notifyTime + '\n\n' + '错误原因:' + '\n\n' + e
        
        print(msg)
        data = {
                    "id": "t5u9mT4",
                    "text": f"{msg}",
                    "type": "json"
                }
        
        
        res = requests.post('http://miaotixing.com/trigger', data=data)
        if res:
            print('喵提醒发送成功')
        else:
            print('喵提醒发送失败')

if __name__ == '__main__':
    a = Cloud_class('账号','密码')
    a.run()
