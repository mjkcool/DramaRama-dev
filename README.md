# DramaRama web service presentation
Made by Python / Use Django, Pandas
  

## Data preparation
- 프로젝트 루트에 위치한 분석할 사전 설문조사 데이터 csv파일을 `dataframe`형태로 불러온다.
- 사전 설문조사 데이터를 바탕으로 수동작업된 드라마 정보 데이터 DB를 `dataframe`형태로 불러온다.
- 가중치 계산을 위해 드라마 정보 데이터 `dataframe`으로부터 드라마 값 테이블을 만든다.
  
<p align="center">
<img width="60%" src="https://user-images.githubusercontent.com/53461080/101436453-8582ad00-3951-11eb-8008-a64083801453.png" />
<br><br>
Form data
<img width="50%" src="https://user-images.githubusercontent.com/53461080/101436551-ba8eff80-3951-11eb-8be7-9b39278289b5.png" />
</p>
<br>

## Solution
- 입력데이터를 사전데이터와 비교해 드라마를 객체로 가중치를 계산하여 최상위 가중치의 드라마 객체를 반환
  - 재이용을 고려해 상위 3개의 드라마 객체 중 랜덤 1개 반환

<p align="center">
<img width="60%" src="https://user-images.githubusercontent.com/53461080/101432006-68e37680-394b-11eb-9fba-b2ab44a142ee.png" />
</p>

```
form_df = form_df.fillna('')  # NaN값 제거
```
### 모든 속성을 비교
```
if col in input_data.keys():  # check there's it
            if type(input_data[col]) == int:
                match = form_df[col] == input_data[col]
                weight_df = form_df[match]
            else:
                for ele in input_data[col]:  # turn all cols in list
                    match = (form_df[col].astype(str)).str.contains(ele)
                    weight_df = pd.concat([weight_df, form_df[match]])

            first = list(weight_df['first'])
            second = list(weight_df['second'])
            third = list(weight_df['third'])
            if not first: continue
            if not second: continue
            if not third: continue
            process_weight(drama_code, first, second, third)  # compute weight
```
### 가중치 계산 함수
```
weight_list = {}  # weight list

def process_weight(drama_code, first, second, third):
    weight = 2  # 가중치
    for step in [first, second, third]:  # type(step) == list
        step = list(filter(lambda e: e != '', step))  # 공백 값 제거
        for elem in step:  # type(elem) == str
            elem = elem.replace(' ', '')  # 글자의 공백제거
            if elem in list(drama_code):
                weight_list[drama_code[drama_code == elem].index[0]] += weight
        weight /= 2
```
