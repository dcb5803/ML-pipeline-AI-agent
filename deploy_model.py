def deploy_model():
    import shutil
    shutil.copy("mlruns/0/latest_model_path", "deployment/model.pkl")
    return "Model deployed"
