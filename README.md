## 환경 설정
* python version: 3.10.x
* 


## 실행

```shell
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

## requirements.txt 만들기
```shell
pipreqs --encoding=utf-8 --force src 
```

## 테스트  
```shell
http://localhost:8080/api/v1/demo?name=windbird123
```
