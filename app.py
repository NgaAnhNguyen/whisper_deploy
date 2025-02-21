import logging
from fastapi import FastAPI, UploadFile, File
import whisper

# Tạo ứng dụng FastAPI
app = FastAPI()

# Cấu hình logging để ghi log chi tiết hơn
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Tải mô hình Whisper
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    try:
        # Ghi nhận thông tin khi nhận yêu cầu
        logger.info(f"Received request to transcribe audio: {file.filename}")
        audio = await file.read()

        # Lưu tệp âm thanh vào hệ thống
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio)
        
        logger.info(f"Audio file {file.filename} saved successfully, starting transcription")

       if "text" in result:
    return {"text": result["text"]}
else:
    return {"error": "No transcription found or audio issue."}
        logger.info("Transcription successful")
        return {"text": result["text"]}

    except Exception as e:
        logger.error(f"Error processing audio oo: {e}")
        return {"error": str(e)}
