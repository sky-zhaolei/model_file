import logging
class Mylogger(logging.Logger):

    def __init__(self,name,level=logging.INFO,file=None):
        #设置输出级别，输出渠道，输出日志格式
        super().__init__(name,level)

        #设置日志输出格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno) line : %(message)s'
        formatter = logging.Formatter(fmt)

        #控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            #控制台渠道
            handle2 = logging.FileHandler(file,encoding='utf-8')
            handle2.setFormatter(formatter)
            self.addHandler(handle2)
if __name__ == '__main__':
    mlogger = Mylogger("py30")
    mlogger.info("测试一下输出的日志内容")




