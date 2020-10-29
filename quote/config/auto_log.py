import logging
import time
class Autolog():
    def __init__(self):
        self.logger = logging.getLogger('log')
    def set_mes(self,mess,level):
        try:
            now_data = time.strftime('%y-%m-%d', time.localtime())
            # 创建文件handle
            fh = logging.FileHandler('../../log_info/auto_' + now_data + '.log',encoding='UTF-8')
            # 创建控制台handle
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
            # 对文件格式
            fh.setFormatter(fm)
            # 对控制台格式
            ch.setFormatter(fm)
            # 文件句柄加入logger
            self.logger.addHandler(fh)
            # 控制台句柄加入logger
            self.logger.addHandler(ch)
            # 设置打印级别
            self.logger.setLevel(logging.DEBUG)
            # 输入info
            if level == 'debug':
                self.logger.debug(mess)
            elif level == 'info':
                self.logger.info(mess)
            elif level == 'warning':
                self.logger.warning(mess)
            elif level == 'error':
                self.logger.error(mess)

            # logger.info('info message')
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台对象
            self.logger.removeHandler(ch)
            # 关闭文件
        except:
            print('file exception')
        finally:
            fh.close()
# if __name__ == '__main__':
#     log=Autolog()
#     url = 'www.baidu.com'
#     log.set_mes('info','打开'+url)
