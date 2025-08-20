times = 2
page_size = 10
code_num =  (times -1) // page_size +1
last_code_num = times % page_size -1
print(code_num,last_code_num)