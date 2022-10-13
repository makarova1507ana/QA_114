import logging
import requests
import funcrion
logging.basicConfig(level='DEBUG',filename='mylog.log', format="[%(asctime)s] - %(levelname)s: %(message)s ")# добавили обрабочка, который закрепелен за логгеров
logger = logging.getLogger()#логгер
logging.getLogger('urllib3').setLevel(logging.CRITICAL)#обратились к постореннему логгеров и выключили его
# print(logger)
# logger.setLevel(logging.DEBUG)
#
# print(logger.level)
# print(logger.handlers)#показывает текущий обрабочких, которые закреплены за текущим логгером
# for key in logging.Logger.manager.loggerDict:
#     print(key)#просмотр текущих логгеров


def main(name):
    logger.debug(f'Enter in the main() function: name={name}')
    #print(dir(logger))#обработчики
    r = requests.get("https://www.google.ru")

def f():
    logger.info("Enter in the f() function:")

if __name__ == '__main__':
    main('Ivan')
    f()
    funcrion.func()
    logger.error("error")