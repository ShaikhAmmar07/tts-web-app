# Backend Deployment (Render)

## Setup

1. Download Piper model:
   - Visit: https://huggingface.co/rhasspy/piper-voices
   - Download: en_US-lessac-medium.onnx
   - Place in `models/` as `en-us.onnx`

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run locally:
   ```
   python app.py
   ```

## Render Deployment

1. Create new Web Service
2. Connect repository
3. Build Command: `bash install_piper.sh && pip install -r requirements.txt`
4. Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. Add model file to repository before deploying
