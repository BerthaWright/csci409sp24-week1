import logging


def factor(num):
    logging.debug(str(num))
    if num > 1:
        return num*factor(num-1)
    else:
        return 1


logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Call factor()')
answer=factor(4)
logging.info('Printing the answer')
print("Answer is", answer)