def num_2_money(num):
    negative = num < 0
    num = abs(num)
    num_ls = str(num).split('.', 1)
    left_res = ""
    left_len = len(num_ls[0])
    comma_num = 0
    for i, _ in enumerate(num_ls[0]):
        ri = (left_len - 1) - i
        left_res = num_ls[0][ri] + left_res
        comma_num += 1
        if comma_num >= 3:
            left_res = "," + left_res
            comma_num = 0
    res = left_res
    if len(num_ls) > 1:
        res = res + "." + num_ls[1]
    if negative:
        res = "-" + res
    return res

