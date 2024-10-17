"""import converter
print(converter.kg_to_lbs(float(input())))
print(converter.lbs_to_kg(float(input())))

#importing specific functions
from converter import kg_to_lbs
#now we can directly call this module like a function
print(kg_to_lbs(70))"""
import functions
print(functions.emoji_converter(message=str(input())))

#each file called a module

import utils
l=list(map(int,input().split()))
print(utils.find_max(l))
