#!/usr/bin/python

import sys, getopt

class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

   

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """

        # method uses employee node and returns an int representing their reports, and descendants
        # for employee, check if there are children nodes
        # children, if they exist, always contained in list
        # if so, count them. if not return 0
        # then call the function recursively on child nodes
        # count_employees("Janet")
        # finds Nick and Nora, counts 2
        # checks for children of Nick and Nora
        # Nick has no children, count stays at 2
        # Nora has 1 child, count increments + 1
        # then callt he function on Nora's child node
        # finds Henri, count increment + 1
        # checks for children of Henri, there are none
        # break out of loop, return count
        
        count = 0 
        
        # continue working see if I can get around the if statements and eliminate them
        # didn't need the if/else statement at all, because count is set to add
        # len(self.children). if no children, count = 0
        # if not self.children:
        #     pass

        # else:
        count += len(self.children)

        for child in self.children:
            inner_count = child.count_employees()
            count += inner_count
            
        return count

henri = Node('Henri')
nora = Node("Nora", [henri])
nick = Node("Nick")
janet = Node("Janet", [nick, nora])
al = Node("Al")
bob = Node("Bob")
jen = Node("Jen")
jessica = Node("Jessica", [al, bob, jen])
jane = Node("Jane", [jessica, janet])

print(jane.count_employees())
print(janet.count_employees())

################################################
##      TESTING ONLY. NO NEED TO UPDATE.      ##
################################################
print("Running some tests...\n")
all_passed = True
if jane.count_employees() == 8:
    print u'\u2714' + " Jane's employees = 8"
else:
    print u'\u2717' + " Jane's employees = 8"
    all_passed = False
if jessica.count_employees() == 3:
    print u'\u2714' + " Jessica's employees = 3"
else:
    print u'\u2717' + " Jessica's employees = 3"
    all_passed = False
if jen.count_employees() == 0:
    print u'\u2714' + " Jen's employees = 0"
else:
    print u'\u2717' + " Jen's employees = 0"
    all_passed = False
if bob.count_employees() == 0:
    print u'\u2714' + " Bob's employees = 0"
else:
    print u'\u2717' + " Bob's employees = 0"
    all_passed = False
if al.count_employees() == 0:
    print u'\u2714' + " Al's employees = 0"
else:
    print u'\u2717' + " Al's employees = 0"
    all_passed = False
if janet.count_employees() == 3:
    print u'\u2714' + " Janet's employees = 3"
else:
    print u'\u2717' + " Janet's employees = 3"
    all_passed = False
if nick.count_employees() == 0:
    print u'\u2714' + " Nick's employees = 0"
else:
    print u'\u2717' + " Nick's employees = 0"
    all_passed = False
if nora.count_employees() == 1:
    print u'\u2714' + " Nick's employees = 1"
else:
    print u'\u2717' + " Nick's employees = 1"
    all_passed = False
if henri.count_employees() == 0:
    print u'\u2714' + " Henri's employees = 0"
else:
    print u'\u2717' + " Henri's employees = 0"
    all_passed = False

if all_passed == False:
    print("\nTest(s) failed! Please try again! :)")
else:
    print("\nAll tests passed! Great job! :)")
