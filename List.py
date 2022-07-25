`import logging
logging.basicConfig(filename="List.log", level=logging.DEBUG, format='[%(levelname)s:%(asctime)s:%(name)s:%(message)s')


class Lists:

    def __init__(self, lists):
        self.lists = lists

    def reverse_list(self):
        logging.debug(" We are going to reverse the given list.")
        try:
            if type(self.lists) != list:
                logging.error("Entered value is not a list.")
            else:
                logging.info("The resultant list is : " + str(self.lists[::-1]))
                return self.lists[::-1]
        except Exception as e:
            logging.error(e)

    def sum_list(self):
        logging.debug(" We are going to calculate the summation of the given list.")
        try:
            if type(self.lists) != list:
                logging.error("Entered value is not a list.")
            for i in self.lists:
                if type(i) != int:
                    logging.error("List contains non integer values. Please provide list containing only integers. ")
            else:
                logging.info(" The resultant list is : " + str(sum(self.lists)))
                return sum(self.lists)
        except Exception as e:
            logging.error(e)

    def extract_list(self):
        logging.debug(" We are going to extract all the lists from the given list. ")
        try:
            if type(self.lists) != list:
                logging.error(" Entered value is not a list. ")
            else:
                a = []
                for i in self.lists:
                    if type(i) == list:
                        a.append(i)
                        logging.debug(" The extracted lists are: " + str(a))
                return a
        except Exception as e:
            logging.error(e)

    def extract_element(self, extract):
        logging.debug(" We are going to extract required element from the list. ")
        try:
            if type(self.lists) != list:
                logging.error(" Entered value is not list. ")
            else:
                b = []
                for i in self.lists:
                    if i == extract:
                        b.append(i)
                    elif type(i) == list or type(i) == set or type(i) == tuple:
                        for j in i:
                            if j == extract:
                                b.append(j)
                    elif type(i) == dict:
                        for k in i.items():
                            if k == extract:
                                b.append(k)
                logging.debug(" The extracted element from the list are : " + str(b))
                return b
        except Exception as e:
            logging.error(e)


l0 = Lists([1, 2, 3, "abc", 4, 5, 6, "efg"])
l1 = Lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
l2 = Lists([1, 2, 3, 4, {1: 2}, {"asv": "Key"}, [5, 6, 7, 8], [9, 10, 11, 12]])
l3 = Lists([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", 'k2': 'ineuron', 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]])
print(l0.reverse_list())
print(l1.sum_list())
print(l2.extract_list())
print((l3.extract_element(45)))
`