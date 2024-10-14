from openai import OpenAI
import os
import edge_tts
import json
import asyncio
import whisper_timestamped as whisper
from utility.script.script_generator import generate_script
from utility.audio.audio_generator import generate_audio
from utility.captions.timed_captions_generator import generate_timed_captions
from utility.video.background_video_generator import generate_video_url
from utility.render.render_engine import get_output_media
from utility.video.video_search_query_generator import getVideoSearchQueriesTimed, merge_empty_intervals
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="동영상의 내용을 바탕으로 짧은 유튜브 쇼츠 영상을 생성한다.")
    parser.add_argument("content", type=str, help="동영상의 내용")

    args = parser.parse_args()
    CONTENT = args.content
    AUDIO_VOICEOVER = "audio_tts.wav"
    VIDEO_SERVER = "pexel"

    response = generate_script(CONTENT)
    print("script: {}".format(response))

    asyncio.run(generate_audio(response, AUDIO_VOICEOVER))

    timed_captions = generate_timed_captions(AUDIO_VOICEOVER)
    print(timed_captions)

    search_terms = getVideoSearchQueriesTimed(response, timed_captions)
    print(search_terms)

    background_video_urls = None
    if search_terms is not None:
        background_video_urls = generate_video_url(search_terms, VIDEO_SERVER)
        print("background video url")
        print(background_video_urls)
    else:
        print("No background video")

    background_video_urls = merge_empty_intervals(background_video_urls)

    if background_video_urls is not None:
        video = get_output_media(AUDIO_VOICEOVER, timed_captions, background_video_urls, VIDEO_SERVER)
        print(video)
    else:
        print("No video")
