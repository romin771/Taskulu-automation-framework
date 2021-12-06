import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)


    fileHandler = logging.FileHandler("taskuluLAutomation.log", mode='a')  # if you want unique name for each specefic log file use : "{0}.log".format(loggerName)
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger


#used in mouseHover file as sample



"""
it will take LogLevel ( info / debug .... ) 
- it can be as function and also as Class, no difference. but we are making it as function because we are using it as API for other files to use it there 
- inspect module in python help us to find :: the name of the class this method is gonna call ( name of the class this method is used there ) 

1) we get the logger  harchi = logging.getLogger(name)   name here is our LoggerName  // from where the log is comming 
2) log all message by default =  logger.setLevel(logging.DEBUG) 
3) define fileHandler = logging.Filehandler(filename="" , mode="") 
4) fileHandler.setLevel...
5) formatter = we want to see in which format our log is define
6) filehandler.setFormatter 


for file handler we should define 1) setLevel and 2) setFormatter 

7) add handler to logger = we are loggin all messages to file     // logger.addHandler(fileHandler)
if you want to log in console, you can replace the Filehandler to screemHandler  

"""