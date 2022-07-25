import logging
logging.basicConfig(filename="Dict.log", level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(name)s:%(message)s')


class Dict:

    def __init__(self, dicts):
        self.dicts = dicts

    def extract_dict(self):
        logging.info(" We are going to extract dict from a given list. ")
        try:
            if type(self.dicts) != list:
                logging.error(" Entered value is not a list. ")
            else:
                r = []
                for i in self.dicts:
                    if type(i) == dict:
                        r.append(i)
                logging.info(" The resultant value is : " + str(r))
                return r
        except Exception as e:
            logging.error(e)

    def extract_dict_element(self):
        logging.info(" We are going to extract elements from a given dict. ")
        try:
            if type(self.dicts) != dict:
                logging.error(" Entered value is not a dict. ")
            else:
                logging.debug(" The resultant value is : " + str(self.dicts.items()))
                return self.dicts.items()
        except Exception as e:
            logging.error(e)


d = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", 'k2': 'ineuron', 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
d1 = Dict(d)
print(d1.extract_dict())

p = {"anirudh": 27, "Vishal": 26, "iNeuron": "Data Science"}
p1 = Dict(p)
print(p1.extract_dict_element())
