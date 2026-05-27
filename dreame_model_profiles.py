MODEL_PROFILES = {
    "dreame.vacuum.r2492j": {
        "profile_key": "dreame.vacuum.r2492j",
        "name": "Dreame L40 Ultra",
    },
    "dreame.vacuum": {
        "profile_key": "dreame.vacuum",
        "name": "Generic Dreame Vacuum",
    },
    "default": {
        "profile_key": "default",
        "name": "Generic Dreame",
    },
}

def get_model_profile(model):
    model = model or "default"
    if model in MODEL_PROFILES:
        return dict(MODEL_PROFILES[model])

    parts = str(model).split(".")
    if len(parts) >= 2:
        family = ".".join(parts[:2])
        if family in MODEL_PROFILES:
            profile = dict(MODEL_PROFILES[family])
            profile["profile_key"] = family + " fallback for " + str(model)
            return profile

    profile = dict(MODEL_PROFILES["default"])
    profile["profile_key"] = "default fallback for " + str(model)
    return profile
