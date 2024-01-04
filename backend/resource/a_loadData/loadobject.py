import pickle

def load_model(path):
    with open(path, 'rb') as f:
        model = pickle.load(f)

    return model

def load_object(path):
    file = open(path,'rb')
    object = pickle.load(file)
    file.close()

    return object
