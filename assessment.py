# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def item_cost_after_tax(item_cost, state_abbr, tax = .05):
    """Takes an item's cost and returns post-tax amout to be paid.

    Default tax rate is set at 5%, unless state is CA, in which case, tax is assumed to be 7%
    """
    
    if state_abbr == "CA":
        tax = .07

    total_cost = item_cost * float(tax)

    return total_cost




#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def is_berry(fruit_name):
    """If the named fruit is a berry, fxn returns True. Otherwise, returns False.
    """

    fruit_list = ["strawberry", "cherry", "blackberry"]

    if fruit_name in fruit_list:
        return True
    else:
        return False

def shipping_cost(fruit_name):
    """ Uses is_bery fxn to determine shipping cost. 0 if it's a berry, otherwise 5.
    """

    if is_berry(fruit_name) == True:
        return 0
    else:
        return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_hometown(town_name):
    """If town_name is "Tampa", returns True, otherwise returns False.
    """

    if town_name == "Tampa":
        return True
    else:
        return False

def full_name(first_name, last_name):
    """Concatenates first and last name.
    """

    return first_name + " " + last_name

def hometown_greeting(hometown, first_name, last_name):
    """Greets user; greeting varies if result from is_hometown is True or False.
    """

    name = full_name(first_name, last_name)

    if is_hometown(hometown) == True:
        print "Hi, %s, we're from the same place!" % (name)

    else:
        print "Hi %s, where are you from?" % (name)


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x = 1):

    y = x

    def add(y):

        return x + y

    add(x)


# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
addfive = increment(5)
addfive = increment(20)


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def generate_list_of_nums(intg, int_list):
    """ Places the intg at the end of the given int_list and returns the int_list with intg at the end.
    """

    int_list.append(intg)

    return int_list

#####################################################################




