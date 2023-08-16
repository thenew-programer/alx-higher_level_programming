#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = {"dummy"}
    common_set.remove("dummy")
    for element in set_1:
        if element in set_2:
            common_set.add(element)
    return common_set
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
