import logging
import traceback
import pandas as pd


def get_data_from_file(file):
    logger = logging.getLogger()
    try:
        df =  pd.read_csv(file, sep=',', header=0, encoding='utf-8') #입력받은 파일의 경로로 파일 read
        parsed_data = df.groupby("분류")['IOC'].apply(list).to_dict() # 분류 칼럼을 기준으로 데이터를 분류 {IOC_type : [data,data2], IOC_type2 : [data3,data4] } 형식
        return parsed_data # 분류된 데이터 반환

    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())


if __name__ == "__main__":
    print(get_data_from_file("IOCS/FamousSparrow-ioc.csv"))
