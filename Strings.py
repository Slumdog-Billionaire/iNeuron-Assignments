import logging
logging.basicConfig(filename="Strings.log",level=logging.DEBUG,format='[%(levelname)s]:%(asctime)s:%(name)s:%(message)s')


class Strings:

    def __init__(self,input_string):
        self.intstr = input_string

#Slicing String with jump of 3 :

    def str_slice_3(self):
        logging.info(" We are about slice the given string in positive direction with a jump of 3")
        try:
            if type(self.intstr) != str:
                logging.error(" Entered value is not a string. ")
            else:
                logging.debug(" The extracted value is : " + self.intstr[:300:3])
                return self.intstr[:300:3]
        except Exception as e :
            logging.error(e)


    def reverse_str(self):
        logging.info(" We are about to reverse the given string. ")
        try:
            if type(self.intstr) != str:
                logging.error(" Entered value is not a string. ")
            else:
                logging.debug(" The extracted value is : " + self.intstr[::-1])
                return self.intstr[::-1]
        except Exception as e :
            logging.error(e)

    def split_upper_str(self):
        logging.info(" We are about to convert str in to lower case and then split it")
        try:
            if type(self.intstr) != str:
                logging.error(" Entered Value is not a string. ")
            else:
                logging.debug(" The extracted value is : " + str(self.intstr.upper().split(" ")))
                return self.intstr.upper().split(" ")
        except Exception as e:
            logging.error(e)

    def lower_case_str(self):
        logging.debug(" We are converting the string into lower case. ")
        try:
            if type(self.intstr) != str:
                logging.debug(" Entered value is not a string. ")
            else:
                logging.debug(" The extracted value is : " + str(self.intstr.lower()))
                return self.intstr.lower()
        except Exception as e:
            logging.error(e)

    def capitalize_str(self):
        logging.debug(" We are capitalizing the string. ")
        try:
            if type(self.intstr) != str:
                logging.debug(" Entered value is not a string.")
            else:
                logging.debug(" The resultant value is : " + str(self.intstr.capitalize()))
                return self.intstr.capitalize()
        except Exception as e:
            logging.error(e)

    def strip_str(self):
        logging.info(" We are conducting the fucntion of strip on the given string.")
        try:
            if type(self.intstr) != str:
                logging.debug(" Entered value is not a string. ")
            else:
                logging.debug(" The resultant value is : " + str(self.intstr.strip()))
                return  self.intstr.strip()
        except Exception as e:
            logging.error(e)

    def lstrip_str(self):
        logging.info(" We are conducting the fucntion of strip on the given string.")
        try:
            if type(self.intstr) != str:
                logging.debug(" Entered value is not a string. ")
            else:
                logging.debug(" The resultant value is : " + str(self.intstr.lstrip()))
                return  self.intstr.lstrip()
        except Exception as e:
            logging.error(e)

    def rstrip_str(self):
        logging.info(" We are conducting the fucntion of strip on the given string.")
        try:
            if type(self.intstr) != str:
                logging.debug(" Entered value is not a string. ")
            else:
                logging.debug(" The resultant value is : " + str(self.intstr.rstrip()))
                return  self.intstr.rstrip()
        except Exception as e:
            logging.error(e)

    def center_str(self,width,symbol):
        logging.debug(" We are going to use Center function on given string. ")
        try:
            if type(self.intstr)!= str:
                logging.error(" Entered value is not a string. ")
            else:
                logging.debug("The resultant value is : " + str(self.intstr.center(width,symbol)))
                return self.intstr.center(width,symbol)
        except Exception as e:
            logging.error(e)




s= Strings('      the Rate of Change of Velocity is called as Acceleration      ')
s1 = Strings("   Just Do It   ")
print(s.str_slice_3())
print(s.reverse_str())
print(s.split_upper_str())
print(s.lower_case_str())
print(s.capitalize_str())
print(s.strip_str())
print(s.lstrip_str())
print(s.rstrip_str())
print(s1.center_str(50,"*"))

























