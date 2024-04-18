
from fastapi import FastAPI
from models import ML
import json
from fastapi.responses import StreamingResponse
from ultralytics import YOLO

url = []
app = FastAPI()

@app.post("/ml")
async def process_url(ml: ML):
    
    # Load a pretrained YOLOv8n model
    model = YOLO('yolov8n.pt')
    # Define path to the image file
    results = model.predict(str(ml.item))
    result = results[0]
    for box in result.boxes:
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)
        print("---")
        url.append({"class_id": class_id, "conf": conf})
      
    return {"values": url}






@app.get("/mlget")
async def get_url():
    return {'hello':'kapil'}



# uvicorn main:app --host 0.0.0.0 --port 80
# uvicorn main:app --reload
# ipconfig http://ipofcomputer/api