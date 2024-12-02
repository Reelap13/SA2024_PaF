from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from api import router as api_router
from queues import queue_api_filter, queue_filter_scream, queue_scream_publish
from services.filter_service import filter_service
from services.scream_service import scream_service
from services.publish_service import publish_service
import multiprocessing

app = FastAPI()

app.include_router(api_router)

def start_processes():
    filter_process = multiprocessing.Process(target=filter_service, args=(queue_api_filter, queue_filter_scream))
    scream_process = multiprocessing.Process(target=scream_service, args=(queue_filter_scream, queue_scream_publish))
    publish_process = multiprocessing.Process(target=publish_service, args=(queue_scream_publish,))

    filter_process.start()
    scream_process.start()
    publish_process.start()

    return [filter_process, scream_process, publish_process]

@app.on_event("startup")
def startup_event():
    global processes
    processes = start_processes()

@app.on_event("shutdown")
def shutdown_event():
    queue_api_filter.put("STOP")
    queue_filter_scream.put("STOP")
    queue_scream_publish.put("STOP")
    for process in processes:
        process.join()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)