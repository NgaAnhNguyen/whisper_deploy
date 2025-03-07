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

        # Chạy quá trình chuyển đổi âm thanh thành văn bản
        result = model.transcribe("temp_audio.mp3")

        # Kiểm tra nếu có văn bản được tạo ra
        if "text" in result:
            return {"text": result["text"]}
        else:
            return {"error": "No transcription found or audio issue."}

    except Exception as e:
        logger.error(f"Error processing audio: {e}")
        return {"error": str(e)}
