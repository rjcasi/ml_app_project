from sklearn.ensemble import RandomForestClassifier

def feature_importance(data, labels):
    model = RandomForestClassifier().fit(data, labels)
    return {"importances": model.feature_importances_.tolist()}
