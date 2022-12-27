def digit(value):
  str_value=str(value)
  for i in range(len(str_value)):
    print(f"{str_value[i]} ,",end=" ") 
print(f"digits in 1234567890 are: ")
digit(1234567890)
def reverse(value1):
    str_value1=str(value1)
    rev_str_value1=str_value1[::-1]
    rev_value1=int(rev_str_value1)
    return rev_value1
print(f"digit in 12345 are:{reverse(12345)}")
def digit(value1):
    str_value1=str(value1)
    rev_str_value1=str_value1[3:6]
    rev_value1=int(rev_str_value1)
    return rev_value1
print(f"digit in 1234567890 are:{reverse(123456890)}")
def reverse(value1):
    str_value1=str(value1)
    rev_str_value1=str_value1[3:5:1]
    rev_value1=int(rev_str_value1)
    return rev_value1
print(f"digit in 1234567890 are:{reverse(123456890)}")
def reverse(value1):
    str_value1=str(value1)
    rev_str_value1=str_value1[:-2]
    rev_value1=int(rev_str_value1)
    return rev_value1
print(f"digit in 123456 are:{reverse(123456)}")
