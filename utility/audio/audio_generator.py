import edge_tts

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate(text,"ko-KR-HyunsuNeural", rate="+20%")
    await communicate.save(outputFilename)





