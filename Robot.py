
def move(input_tuple):
    pos_x,pos_y= input_tuple[0]
    for command in input_tuple [1]:
        if command=='R':
            pos_x= pos_x+1
        elif command== 'L':
            pos_x==pos_x-1
        elif command=='U':
            pos_y==pos_y+1
        elif command=='D':
            pos_y=pos_y-1
        else:
            raise ValueError('invalid command to robot')
    return (pos_x,pos_y)
print(move (((3,-8),"RRDDL")))
