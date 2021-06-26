import time
from src.lambda_function import lambda_handler
while True:
    time.sleep(10)    
    lambda_handler(None,None)
    