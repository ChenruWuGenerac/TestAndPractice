import logging

# test1: if run warning and info first then call basicConfig
# it will still be the default level, the basicConfig make no
# effects here

# logging.warning("I told you so")
# logging.info("this is a information from logging")

# print("----------------")

logging.basicConfig(
    level=logging.DEBUG,
)

logging.warning("I told you so")
logging.info("this is a information from logging")


# test2 logging in file
# import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
