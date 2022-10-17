import os
import pandas as pd
import logging
import traceback
dir = "IOCS"

def open_file(file):
    logger = logging.getLogger()
    try:
        with pd.read_csv(os.path.join(dir,file) , sep=',',header=0, encoding='utf-8') as df:
            parse_data = df.groupby("분류")['IOC'].apply(list).to_dict()
            return parse_data
        
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
    
    
if __name__=="__main__":
    open_file("FamousSparrow-ioc.csv")