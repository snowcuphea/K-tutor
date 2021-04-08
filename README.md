# A303 - 말뭉치(K-tutor)

<div align=center>
    <img src="https://img.shields.io/badge/platform-web-green">
    <img src="https://img.shields.io/badge/framwork-Vue-42b883">
    <img src="https://img.shields.io/badge/framework-django-blue">
    <img src="https://img.shields.io/badge/database-MariaDB-9cf">
    <img src="https://img.shields.io/badge/server-AWS-yellow">
    <img src="https://img.shields.io/badge/language-python%2C javascript-yellowgreen">
    <img src="https://img.shields.io/badge/swagger-valid-brightgreen">
</div>



**외국인을 대상으로 구어체 빅데이터와 한류컨텐츠(K-drama, K-movie, K-pop)를 이용하여 한국어 학습을 제공하는 모바일 전용 Web 서비스**

* 수행 기간:  2021.02.26 ~ 2021.04.09 

* 결과물 : http://j4a303.p.ssafy.io:8080 (Web)

* UCC :






## 목차

### [팀원소개](#팀원소개) 

### [기술스택](#기술스택)

### [구동방법](#구동방법)

### [기능소개](#기능소개)



## 팀원소개

> 수행 인원 : 5명

* 고영길 - Backend

* 김동준 - Backend
* 김동현 - Frontend

* 김민정 - Frontend

* 이건우 - Frontend





## 기술스택

### Bigdata 분석

| python 라이브러리 | Version | Comment                    |
| :---------------: | :-----: | :------------------------- |
|      Pandas       |  1.2.3  | 데이터 조작 및 분석        |
|      KoNLPy       |  0.5.2  | 자연어 처리 및 형태소 분석 |
|      Gensim       |  3.8.3  | 데이터 학습 모델링         |



### Backend 구성 요소

| 기술 스택 |   Version   | Comment                             |
| :-------: | :---------: | :---------------------------------- |
|  python   |    3.7.7    |                                     |
|  Django   |    3.1.7    | Rest API 웹 애플리케이션 개발       |
|  MariaDB  |   10.5.9    | DB                                  |
|  Ubuntu   | 20.04.2 LTS | 서비스 제공을 위해 리눅스 서버 구축 |
|  Docker   |   20.10.2   | 컨테이너화 된 애플리케이션 관리     |
|   Nginx   |   1.19.6    | 웹서버, 서버 프록시                 |

### Frontend 구성 요소

| Vue 라이브러리 | Version | Comment                                |
| :------------: | :-----: | :------------------------------------- |
|     axios      | 0.21.1  | 서버로 요청을 보내기 위해 사용         |
|   vue-router   |  3.2.1  | 요청 URL에 따라 브라우저에서 돔을 변경 |
|      vuex      |  3.4.0  | 상태 관리를 위해 사용                  |
|    vuetify     |  2.4.0  | UI 구성을 위해 사용                    |
|    chart.js    |  2.9.4  | 파형을 나타내기 위한 라이브러리        |
| vuex-persistedstate |  4.0.0 | Store의 state 값 초기화를 방지하기 위해 사용 |





## 구동방법



### Server

```bash
# Install Docker , docker-compose
curl -fsSL https://get.docker.com/ | sudo sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Docker-compose
docker-compose up

# Without Docker
gunicorn server.wsgi:application --bind 0.0.0.0:8000

# or 

python manage.py runserver
```









### Client

```bash
######## ver. npm ###########
# Project Setup
npm install

# Compiles and hot-reloads for development
npm run serve



######### ver. yarn ##########
# Project Setup (ver. npm)
yarn install

# Compiles and hot-reloads for development
yarn serve
```



## 기능소개

### 1. Class

> 사용자가 학습을 진행하는 공간

* 학습 현황 확인 (프로그레스바)

* 테마 선택 (K-drama, K-movie, K-pop) > 작품 선택 > 키워드 선택 > 학습카드로 학습

* 학습카드 구성 (총 3장)

  ​	1) 키워드 및 전 후 상황 대사(가사) 노출

  ​	2) 키워드 설명, 해석, 활용 예제 

  ​	3) 키워드 중심 문장 나열 연습

* Quiz

  * 학습카드 5개 이상 학습 시 활성화
  * 사용자가 학습한 내용을 토대로 문제 제출
  * 하루에 3번까지만 가능 (경험치 어뷰징 방지)

  

### 2. Test

> 사용자가 학습한 내용을 토대로 시험을 보는 공간

* 성적표 차트 
* 테스트
  * 10문제로 구성
  * 사용자가 클래스에서 학습한 내용과 새로운 문제를 섞어 출제
  * 점수에 따른 경험치 상승
  * 하루에 2번까지만 가능 (경험치 어뷰징 방지)



### 3. Report

> 사용자의 학습 기록 및 학습 현황 확인 페이지

* 연속 출석일
* 총 학습한 학습카드 수
* 최근 학습한 카드 리스트
* 총 학습 진행 현황



### 4. Achieve

> Gamification을 접목한 업적 페이지.

* 사용자가 서비스를 사용하면서 조건 달성 시 특정 뱃지 획득 (음영 -> 컬러처리)
* 뱃지는 한국 문화를 대표하는 일러스트로 제공

* 그리드형, 설명형 2가지 방식으로 UI 제공
* 업적 달성 시 한국 문화에 대한 설명 및 위키url 제공



### 5. My Page

> 사용자의 정보 확인/수정, 튜토리얼 등 계정 및 서비스 정보 내용 페이지

* 계정 정보

  * 레벨에 따른 프로필 사진 (저레벨: 평민, 중레벨: 양반, 고레벨: 고위양반, 최고레벨: 왕)
  * 닉네임, 이메일
  * 정보 수정
    * 닉네임,  비밀번호 수정
    * 조선시대 이름 짓기 기능 (월, 일 입력)

* 튜토리얼

  * 말뭉치(K-tutor) 서비스 사용법 제공

* 문의하기

  * 서비스 관리자에게 문의할 수 있는 기능 제공

* 이용약관

* 라이선스

  * 사용한 오픈소스 및 라이브러리 출처 명시
  * 폰트 출처 명시

* 로그아웃

* 회원탈퇴

  







