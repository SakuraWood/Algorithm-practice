class BiMap(object):
    def __init__(self):
        self.dict1 = {}
        self.dict2 = {}

    def put(self, k, v):
        if not self.dict2.has_key(v):
            self.dict1[k] = v
            self.dict2[v] = k
        else:
            raise Exception('value can not be duplicated')

    def get_value_for_key(self, k):
        return self.dict1[k]

    def get_key_for_value(self, v):
        return self.dict2[v]
