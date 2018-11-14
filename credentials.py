import yaml as yml

def Loadcredentials(id):
  ar = []
  stream = open("twitter_keys.yaml", "r")
  docs = yml.load_all(stream)
  for doc in docs:
    for k,v in doc.items():
      ar.append(v)
  return ar[id]



