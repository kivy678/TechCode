# -*- coding:utf-8 -*-

##########################################################################
import pandas as pd
import numpy as np

##########################################################################



######################################## 데이터 프레임 생성 ########################################


COLUMNS_NAME = [
    'colume1',
    'colume2',
    'colume3',
]

class DATAFRAME_EXCEPTION_HANDER(Exception): pass


PANDAS_EXAMPLE = pd.DataFrame(columns=COLUMNS_NAME)
CSV_EXAMPLE = None

try:
    csv_file = pd.read_csv("data.csv", sep=',', index_col=0)                    # csv 를 읽어서 데이터 프레임으로 변경
    if csv_file is None:
        raise DATAFRAME_EXCEPTION_HANDER('Could not load csv.')

    CSV_EXAMPLE = pd.DataFrame(data=csv_file)
    CSV_EXAMPLE = CSV_EXAMPLE.where(pd.notnull(CSV_EXAMPLE), '')

    #CSV_EXAMPLE.to_csv("write path", mode='w')
    
except DATAFRAME_EXCEPTION_HANDER as e:
    print(e)



######################################## 컬럼 추가 및 접근 ########################################
PANDAS_EXAMPLE.index.name = 'id'

print(PANDAS_EXAMPLE.head())      # 테이블 확인

for idx in range(10):
    add_idx = pd.Series({"colume1": str(idx+10)}).rename(idx)   # 인덱스 및 컬럼에 데이터를 동시에 추가 가능
    PANDAS_EXAMPLE = PANDAS_EXAMPLE.append(add_idx)


print(PANDAS_EXAMPLE.index.tolist())                           # 인덱스를 리스트로 가져오기


print("[*]: " + PANDAS_EXAMPLE.loc[3, 'colume1'])                           # 인덱스를 통한 컬럼 접근
print("[*]: " + PANDAS_EXAMPLE.loc[3].get(key='colume1', default=None))     # get 메소드를 통한 컬럼 접근


file_data = {
    'colume1': 'aaa',
    'colume2': 'bbb',
    'colume3': 'ccc',
}

PANDAS_EXAMPLE.loc[5] = pd.Series(file_data)                                # row에 데이터 넣기
PANDAS_EXAMPLE.loc[5, 'colume1'] = "ddd"                                    # 단일 컬럼에 데이터 넣기

#PANDAS_EXAMPLE = np.array(PANDAS_EXAMPLE).T[1].tolist()

PANDAS_EXAMPLE = PANDAS_EXAMPLE[~PANDAS_EXAMPLE.index.duplicated(keep='first')]       # 첫행을 제외한 인덱스 중복 제거



######################################## 추가 기능 ########################################
PANDAS_EXAMPLE.reset_index(inplace=True, drop=True)     # 인덱스 리셋
PANDAS_EXAMPLE.index.name = 'id'
print(PANDAS_EXAMPLE.head())
print(PANDAS_EXAMPLE.last_valid_index())


PANDAS_EXAMPLE = PANDAS_EXAMPLE.groupBy("").pivot("")                       # 선택한 컬럼을 열로 변경한다.


#df.iterrows() < df.itertuples()   #### itertuples 성능이 더 좋다고 한다. iterable 를 사용할 때는 iteruples 를 사용하자
