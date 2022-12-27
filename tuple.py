buffet_tuple=('salad','roti','curry','rice','dessert')
for i ,item in enumerate(buffet_tuple):
    print(f"item no.{i+1}in buffet is {item}")
index= buffet_tuple.index('rice')
print(index)
revised_buffet_tuple = (buffet_tuple[0], 'Naan', buffet_tuple[2], \
                        buffet_tuple[3], 'Ice-cream')
print("This is revised menu of the Buffet.")
for i,item in enumerate(revised_buffet_tuple):
  print(f"Item No. {i+1} in the Buffet is {item}.")