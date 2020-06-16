import logging
import logging.handlers


def setup_logger(name, filename="./test_complete_loc.log", stream=False, save=False, top=False, level=logging.DEBUG):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')

    if stream:
        logger.setLevel(level)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if save:
        logger.setLevel(level)
        handler = logging.handlers.RotatingFileHandler(
                filename,
                mode='a',
                maxBytes=50*1024*1024,
                backupCount=10,
                encoding='utf-8'
            )
        # handler = logging.FileHandler(filename)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    if top:
        logger.addHandler(logging.NullHandler())

    return logger