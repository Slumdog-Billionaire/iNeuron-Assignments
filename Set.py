import logging
logging.basicConfig(filename="Set.log", level=logging.DEBUG, format="%(levelname)s:%(name)s:%(asctime)s:%(message)s")


class Set:

    def __init__(self, sets):
        self.sets = sets

    def extract_set(self):
        logging.debug(" We are going to extract tuple from a given list. ")
        try:
            n = []
            for i in self.sets:
                if type(i) == set:
                    n.append(i)
            logging.info(" The resultant value is : " + str(n))
            return n
        except Exception as e:
            logging.error(e)

    def extract_unique_set(self):
        logging.debug(" We are going to extract unique set from a given list. ")
        try:
            if type(self.sets) != list:
                logging.error(" Entered value is not a list")
            else:
                if type(self.sets) == list:
                    logging.info(" The resultant value is : " + str(set(self.sets)))
                    return set(self.sets)

        except Exception as e:
            logging.error(e)


s = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", 'k2': 'ineuron', 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
s1 = Set(s)
print(s1.extract_set())

p = [2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8]
p1 = Set(p)
print(p1.extract_unique_set())
