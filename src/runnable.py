import time
from lambda_function import lambda_handler
while True:
    lambda_handler(None,None)
    time.sleep(10)    
    