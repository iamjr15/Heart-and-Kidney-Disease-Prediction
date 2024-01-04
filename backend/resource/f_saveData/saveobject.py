import pickle

def save_object(object, path):
    filehandler = open(path,"wb")
    pickle.dump(object,filehandler)
    filehandler.close()

def save_model(model,path):
    with open(path, 'wb') as f:
        pickle.dump(model, f)
