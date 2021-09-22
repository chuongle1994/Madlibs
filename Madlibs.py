from random import randint
import copy
story=("My name is Chuong Le "+ "I have visited to {}. "+ "I love {} dog and cat. "+"I like to {} with my friends. ")
dic={
    "noun":["NewYork","Boston","Chicago"],
    "adjective":["beautiful","friendly","funny"],
    "activity":["cook","play soccer","hang out"]
}
#create a function 
def get_word(type,local_dict):
    words = local_dict[type]
    index = randint(0,len(words)-1)
    return local_dict[type].pop(index)

    
def create_function():
    local_dict = copy.deepcopy(dic)
    return story.format(
        get_word("noun",local_dict),
        get_word("adjective",local_dict),
        get_word("activity",local_dict),
    )
print("Story 1: ")
print(create_function())
print()
print("Story 2: ")
print(create_function())