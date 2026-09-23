from io import BytesIO
from gtts import gTTS


class TextToSpeech:
    def speak(self, text, lang="en"):
        print("🔊 TTS CALLED:", text)
        cleaned = (text or "").strip()

        if not cleaned:
            print("❌ TTS RECEIVED EMPTY TEXT")
            return
        
        buffer = BytesIO()

        gTTS(text=cleaned, lang=lang).write_to_fp(buffer)

        buffer.seek(0)
        print("✅ AUDIO GENERATED")

        return buffer.read()
    