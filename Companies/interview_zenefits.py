# code interview solution for company Zenefits
# 2019-11-15

"""
Assumption: data structure is valid (no any additional validation needed)
Given Input as matrix M with size Nx4, where :
M[1][0] - employee name
M[1][1] - employee boss name
M[1][2] - employee role
M[1][3] - employee location

"DD","Glynn","Dev","SF"
"Avi","Laks","VP","SF"
"Dave","Avi","Dev","Canada"
"Hari","DD","Dev","India"
"Jin","Glynn","Dev","SF"
"Ram","Avi","Dev","SF"
"Laks","Laks","CEO","SF"
"Glynn","Laks","Principal Engineer","SF"
"Laura","Laks","Senior Staff","Canada"


Build Output like in example, hierarchical structure:

Laks [CEO, SF]
    Avi [VP, SF]
        Dave [Dev, Canada]
        Ram [Dev, SF]
    Glynn [Principal Engineer, SF]
        DD [Dev, SF]
            Hari [Dev, India]
        Jin [Dev, SF]
    Laura [Senior Staff Engineer, Canada]
"""

given_data = [
    ["DD","Glynn","Dev","SF"],
    ["Avi","Laks","VP","SF"],
    ["Dave","Avi","Dev","Canada"],
    ["Hari","DD","Dev","India"],
    ["Jin","Glynn","Dev","SF"],
    ["Ram","Avi","Dev","SF"],
    ["Laks","Laks","CEO","SF"],
    ["Glynn","Laks","Principal Engineer","SF"],
    ["Laura","Laks","Senior Staff","Canada"],
]


# just OOP god style have DAO for object
class Person:
    def __init__(self, name, parent, position, location):
        self.name = name
        self.parent = parent
        self.position = position
        self.location = location
        self.children = []
        self.indent = 0 # printing indent

    # default print / tostring format
    def __repr__(self):
        return "     " * self.indent + "%s [%s, %s]" % (self.name, self.position, self.location)


# pretty straight forward solution with dictionary helper
def execute_task(matrix_data):
    person_dic = {}
    for pers_item in matrix_data:
        p = Person(pers_item[0], pers_item[1], pers_item[2], pers_item[3])
        person_dic[p.name] = p

    root = None

    for pers_item in person_dic.values():
        if not root and pers_item.name == pers_item.parent:
            root = pers_item
        else:
            person_dic[pers_item.parent].children.append(pers_item)

    print_children(root)


# recursive print with indent calculation
def print_children(person_item):
    print(person_item)
    for child in person_item.childs:
        child.indent = 1 + person_item.indent
        print_children(child)


execute_task(given_data)
















