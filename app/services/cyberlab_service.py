import random
import string

def fuzz(seed):
    random.seed(seed)
    return {"attack": ''.join(random.choices(string.ascii_letters, k=12))}

def defend(pattern):
    safe = pattern.replace("A", "*")
    return {"defended": safe}
