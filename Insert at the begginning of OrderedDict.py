from collections import OrderedDict
iniordered_dict = OrderedDict([('Nike', '1'), ('John', '2')])

iniordered_dict.update({'Fran': '3'})
iniordered_dict.move_to_end('Fran', last=False)
print("Resultant Dictionary : " + str(iniordered_dict))