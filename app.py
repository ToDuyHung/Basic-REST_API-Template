from fastapi import FastAPI
import uvicorn

from utils.logging_utils import setup_logging
from config.config import Config
from data_models.data_models import Product
from process.processor import Processor

app = FastAPI()
_config = Config()
setup_logging(logging_folder=_config.logging_folder, log_name=_config.log_name)
processor = Processor(config=_config)

@app.post("/image_attribute_extraction")
async def image_attribute_extraction(input_data: Product):
    response = await processor.process(input_data)
    return response

if __name__ == "__main__":
    uvicorn.run("app:app", host='localhost', port=8080, reload=True, debug=True, workers=1)
    