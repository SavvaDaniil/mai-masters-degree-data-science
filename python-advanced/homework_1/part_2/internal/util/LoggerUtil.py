import logging
from internal.singleton.SingletonMeta import SingletonMeta


logger = logging.getLogger('WarehouseLogger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('warehouse.log', 'a', 'utf-8')
file_handler.setLevel(logging.DEBUG)

log_format = logging.Formatter('%(asctime)s – %(name)s – %(levelname)s – %(message)s', datefmt='%H:%M:%S')
file_handler.setFormatter(log_format)

logger.addHandler(file_handler)
