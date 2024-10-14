# 챗GPT 유튜브 쇼츠 생성기 🎬

내용만 입력하면 유튜브 쇼츠 영상을 생성합니다.
한국형 쇼츠에 최적화됐습니다.

작동 방식은 다음과 같습니다:
1. 내용을 바탕으로 영상 스크립트 생성
2. 스크립트를 엣지 tts를 사용하여 음성화
3. 음성을 내용별로 나눈 후 캡션 생성
4. Pexels를 통해 캡션과 알맞는 배경 영상 다운로드
5. 배경 영상, 캡션, 음성 합성 후 완성

### 다음과 같은 동영상이 생성됩니다.

[rendered_video (2).webm](https://github.com/user-attachments/assets/63cd5b83-aa44-4083-a946-bdbeccf57673)


### 스타를 눌러주시면 감사하겠습니다.
챗GPT 유튜브 쇼츠 생성기를 잘 사용하신다면 스타를 눌러주세요!
여러분의 관심을 통해 프로젝트를 업그레이드합니다.

[![GitHub star chart](https://img.shields.io/github/stars/LighterLinks/Korean_Shorts_AI?style=social)](https://github.com/LighterLinks/Korean_Shorts_AI/stargazers)

### 실행하기
#### 1. 환경 설정

레포지토리를 클론하고 필요한 환경을 설치합니다.
파이썬 3.11 환경을 권장합니다

```
git clone https://github.com/LighterLinks/Korean_Shorts_AI.git
cd Korean_Shorts_AI
pip install -r requirements.txt 
```
동영상 위에 캡션을 달기 위해 ImageMagick과 ffmpeg이라는 라이브러리가 필요합니다.

리눅스 :
```
sudo apt install imagemagick ffmpeg
```

만약 프로그램 실행시 moviepy 라이브러리가 imagemagick 바이너리를 찾을 수 없다는 에러가 난다면 imagemagick 의 policy 파일을 수정해야 합니다.
/etc/ImageMagick-6/policy.xml 파일을 수정해서 다음 줄을 삭제하면 됩니다.
```
<policy domain="path" rights="none" pattern="@*" />
```

#### 2. API 키 생성 및 Export
동영상을 생성하기 위해 오픈AI와 Pexels의 API키가 필요합니다.
Pexels는 무료로 이용할 수 있습니다.
키 생성후 다음과 같이 Export 합니다.
```
export OPENAI_KEY="오픈AI_API_키"
export PEXELS_KEY="Pexels_API_키"
```


#### 3. 동영상 생성
쇼츠 영상의 내용을 입력하면 동영상이 생성됩니다.
예를 들어, 24년 노벨 문학상 수상자인 한강 작가에 대한 영상을 만들어 보겠습니다.

```
python app.py "한강 작가는 1970년 광주에서 태어난 한국의 소설가입니다.
연세대학교 국문학과를 졸업한 후, 1993년 문단에 등단하면서 문학 활동을 시작했습니다. 
그녀는 다수의 소설을 집필하였으며, 대표작으로는 <채식주의자>, <소년이 온다>, <작별하지 않는다> 등이 있습니다.
한강은 2016년 소설 <채식주의자>로 맨부커상 국제 부문을 수상하며 국제적으로 주목받기 시작했습니다. 
그녀의 작품들은 주로 인간의 내면과 사회적 폭력, 소통의 부재 등을 탐구하는 내용으로 구성되어 있습니다.
2024년, 한강은 한국인 최초로 노벨 문학상을 수상하였으며, 이는 한국 문학사에 있어 큰 쾌거로 평가받고 있습니다. 
노벨상 수상작으로 선정된 작품 <작별하지 않는다>는 5·18 광주 민주화 운동을 배경으로 한 역사적 서사와 개인적 고통의 이야기를 담고 있습니다.
 한강의 문학은 독특한 시적 표현과 인간 존재에 대한 깊은 통찰로 많은 독자들에게 감동을 주고 있습니다."
```

맨 위의 동영상이 생성됩니다.


## 💁 기여하기
오픈소스 프로젝트로서 우리는 기여에 매우 열려 있습니다. 시작하려면 Github에서 문제를 제기하거나 pull request를 만드세요.


