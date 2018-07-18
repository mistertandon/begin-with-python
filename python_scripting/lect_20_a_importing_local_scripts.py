import lect_20_b_useful_functions as m_uf

list_nums = [4, 3, 8]
cal_mean = m_uf.mean(list_nums)
print("\n mean of list [4, 3, 8] is {}".format(cal_mean))

print("\n Adding integer 5 to each element in list\n")
list_nums_update = m_uf.add_five(list_nums)
print(list_nums_update)
