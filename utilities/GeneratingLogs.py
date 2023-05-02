import logging

class log001:
    @staticmethod
    def generate_log():

        logging.basicConfig(
            filename="C:\\Users\\91789\\PycharmProjects\\miniProject\\reports\\miniproject01.log",
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S %p'
        )
        logger=logging.getLogger()
        logger.setLevel(level="INFO")
        return logger

