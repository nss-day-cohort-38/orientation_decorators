# In Python, we can pass functions as arguments, functions can be return values and we can have a function within a function. This allows us to write higher order functions.
# def add_things(x,y):
#     def concat_first_last():
#         return x() + " " + y()
#     return concat_first_last

# def first_name():
#     return "Jisie"

# def last_name():
#     return "David"


# new_thing = add_things(first_name, last_name)
# print(new_thing)
# print(new_thing())

# Decorators

def reversal(sentence_func):
    # It is very common to use *args and **kwargs for the wrapper function. That way, it will accept an arbitrary number of positional and keyword arguments.
    def reversed_sentence(*args, **kwargs):
        # By continuing to use *args and **kwargs, all arguments are passed to the function that is being decoarated.
        original_sentence = sentence_func(*args, **kwargs)
        return f"Reversed: {''.join(reversed(original_sentence))}"
    return reversed_sentence


@reversal
def letterPress():
    return f"Adaptogen tote bag drinking vinegar, letterpress pabst locavore migas hella"

# Equivalent to:
#letterPress = reversal(letterPress)
#letterPress()


def taxidermy():
    return "Taxidermy health goth locavore, pickled post-ironic pork belly kale chips tofu PBR&B bicycle rights"


@reversal
def mustache():
    return "Umami hexagon stumptown enamel pin, mustache echo park readymade celiac"


def lumberSexual():
    return "Jean shorts lumbersexual stumptown tumeric everyday carry readymade"


print(letterPress())
print(taxidermy())
print(mustache())
print(lumberSexual())
