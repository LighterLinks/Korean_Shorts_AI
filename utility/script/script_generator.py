import os
from openai import OpenAI
import json


OPENAI_API_KEY = os.getenv('OPENAI_KEY')
model = "gpt-4o"
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_script(content):
    prompt = (
        """당신은 YouTube Shorts 채널의 노련한 콘텐츠 작가로 숏폼 동영상 스크립트 생성을 전문으로 합니다.
쇼츠 영상 50초(약 140단어) 미만이여야 합니다.
제공된 내용을 바탕으로 쇼츠 영상의 스크립트를 만들며 이는 매력적이며 독창적이여야 합니다.
스크립트는 아무런 이모티콘이나 특이한 모양 없이 플레인 텍스트로 만들어야 합니다.

사용자가 제공한 내용을 바탕으로 아래와 같이 스크립트를 JSON 형식으로 출력하고, 키 'script'가 있는 구문 분석 가능한 JSON 객체만 제공하세요.

# 출력
{"script": "여기 스크립트가 있습니다..."}
"""
    )

    response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": content}
            ]
        )
    content = response.choices[0].message.content
    try:
        script = json.loads(content)["script"]
    except Exception as e:
        json_start_index = content.find('{')
        json_end_index = content.rfind('}')
        print(content)
        content = content[json_start_index:json_end_index+1]
        script = json.loads(content)["script"]
    return script
