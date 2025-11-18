import logging
import logging.handlers

def setup_logger(queue):
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)

    # Create a queue handler
    queue_handler = logging.handlers.QueueHandler(queue)
    logger.addHandler(queue_handler)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Create a formatter and set it for the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    queue_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(console_handler)

    return logger
