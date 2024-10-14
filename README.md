# 챗GPT 유튜브 쇼츠 생성기 🎬

간단한 내용을 입력하면 유튜브 쇼츠 영상을 자동으로 생성합니다.  
한국형 쇼츠에 최적화된 AI 기반 동영상 생성기입니다.

## 작동 방식:
1. 입력된 내용을 바탕으로 영상 스크립트 생성
2. 생성된 스크립트를 엣지 TTS를 사용해 음성화
3. 음성을 내용별로 나누고, 자동으로 캡션 생성
4. Pexels에서 캡션과 적합한 배경 영상을 다운로드
5. 배경 영상, 캡션, 음성을 합성해 완성된 동영상 출력

### 예시 영상


https://github.com/user-attachments/assets/a9dadb1e-d533-43dc-84e1-53b699f96531



---

### ⭐️ 스타를 눌러주세요!
챗GPT 유튜브 쇼츠 생성기를 유용하게 사용하셨다면, 스타를 눌러주세요!  
여러분의 피드백과 관심은 이 프로젝트의 성장을 돕습니다.

[![GitHub 스타](https://img.shields.io/github/stars/LighterLinks/Korean_Shorts_AI?style=social)](https://github.com/LighterLinks/Korean_Shorts_AI/stargazers)

---

## 🚀 실행 방법

### 1. 환경 설정
레포지토리를 클론하고 필요한 패키지를 설치하세요.  
파이썬 3.11 환경을 권장합니다.

```bash
git clone https://github.com/LighterLinks/Korean_Shorts_AI.git
cd Korean_Shorts_AI
pip install -r requirements.txt
```

동영상에 캡션을 추가하기 위해 **ImageMagick**과 **ffmpeg** 라이브러리가 필요합니다.

#### 리눅스 설치 방법:
```bash
sudo apt install imagemagick ffmpeg
```

만약 프로그램 실행 중 `moviepy` 라이브러리가 `ImageMagick` 바이너리를 찾을 수 없다는 오류가 발생하면,  
다음과 같이 `ImageMagick`의 정책 파일을 수정해야 합니다.

`/etc/ImageMagick-6/policy.xml` 파일에서 다음 줄을 삭제하세요. 파일의 가장 아래에 있습니다 :
```xml
<policy domain="path" rights="none" pattern="@*" />
```

### 2. API 키 생성 및 설정
동영상 생성을 위해 OpenAI와 Pexels의 API 키가 필요합니다.  
Pexels는 무료로 이용할 수 있습니다. API 키를 생성한 후, 아래와 같이 설정합니다:

```bash
export OPENAI_KEY="오픈AI_API_키"
export PEXELS_KEY="Pexels_API_키"
```

### 3. 동영상 생성
원하는 내용을 입력하면 자동으로 쇼츠 영상이 생성됩니다.  
예를 들어, 2024년 노벨 문학상 수상자인 한강 작가에 대한 영상을 만들어 보겠습니다:

```bash
python app.py "한강 작가는 1970년 광주에서 태어난 한국의 소설가입니다. 연세대학교 국문학과를 졸업한 후, 1993년 문단에 데뷔하며 문학 활동을 시작했습니다. 그녀는 다수의 소설을 집필하였으며, 대표작으로는 <채식주의자>, <소년이 온다>, <작별하지 않는다> 등이 있습니다. 2016년 <채식주의자>로 맨부커상 국제 부문을 수상하며 국제적 주목을 받았습니다. 2024년, 한강은 한국인 최초로 노벨 문학상을 수상하며, 이는 한국 문학사에 있어 큰 쾌거로 평가받고 있습니다."
```

위와 같은 입력으로 동영상이 생성됩니다.

---

## 💁 기여하기
이 프로젝트는 오픈소스이며, 여러분의 기여를 환영합니다!  
문제를 제기하거나, pull request를 보내주세요.
