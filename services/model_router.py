def choose_model(mode):

    model_map = {
        "panic": "llama-3.3-70b-versatile",
        "war": "llama-3.3-70b-versatile",
        "anxiety": "llama-3.3-70b-versatile",
        "calm": "llama-3.3-70b-versatile",
        "support": "llama-3.3-70b-versatile",
        "integration": "llama-3.3-70b-versatile",
        "general": "llama-3.3-70b-versatile"
    }

    return model_map.get(mode, "llama-3.3-70b-versatile")