def check_performance_and_trigger():
    from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex

    docs = SimpleDirectoryReader("logs").load_data()
    index = GPTVectorStoreIndex.from_documents(docs)
    query_engine = index.as_query_engine()
    response = query_engine.query("Is model accuracy below 0.85?")
    if "yes" in str(response).lower():
        from pipeline.train_model import train_model
        return train_model()
    return "Performance is acceptable"
