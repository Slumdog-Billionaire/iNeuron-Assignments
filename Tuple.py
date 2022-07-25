import logging
logging.basicConfig(filename="Tuple.log", level=logging.DEBUG, format="%(levelname)s:%(asctime)s:%(name)s:%(message)s")


class Tuple:

    def __init__(self, tuples):
        self.tuples = tuples

    def extract_tuple(self):
        logging.debug(" We are going to extract tuples from a list")
        try:
            m = []
            for i in self.tuples:
                if type(i) == tuple:
                    m.append(i)
            logging.debug(" The resultant value is : " + str(m))
            return m
        except Exception as e:
            logging.error(e)

    def extract_element(self, start, stop, step=1):
        logging.debug(" We are going to extract required elements from the variable.")
        try:
            logging.info(" The resultant value is : " + str(self.tuples[start:stop:step]))
            return self.tuples[start:stop:step]
        except Exception as e:
            logging.error(e)


t = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {[23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]}, {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
t1 = Tuple(t)
print(t1.extract_tuple())
k = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
k1 = Tuple(k)
print(k1.extract_element(3, 8))
