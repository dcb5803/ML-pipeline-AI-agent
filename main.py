from fastapi import FastAPI
from pipeline import data_collection, preprocessing, train_model, evaluate_model, deploy_model
from agent import monitor_logs

app = FastAPI()

@app.get("/run_pipeline")
def run_pipeline():
    steps = []
    steps.append(data_collection.collect_data())
    steps.append(preprocessing.preprocess_data())
    steps.append(train_model.train_model())
    steps.append(evaluate_model.evaluate_model())
    steps.append(deploy_model.deploy_model())
    return {"pipeline": steps}

@app.get("/monitor")
def monitor():
    result = monitor_logs.check_performance_and_trigger()
    return {"monitor_result": result}
