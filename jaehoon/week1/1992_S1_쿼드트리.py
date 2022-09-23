def check(board,size):
    flat_board = [n for row in board for n in row]
    for i in range(size**2):
        if flat_board[0] != flat_board[i]:
            return False
    return True 

def divide(board,size):
    if size==2:
        if check(board,size):
            print(board[0][0],end='')
        else:
            print('(',end='')
            for i,j in board:
                print(i,end='')
                print(j,end='')
            print(')',end='')
        return
    
    if check(board,size):
        print(board[0][0],end='')
        return
    else:
        print('(',end='')
    
    arr1,arr2,arr3,arr4,temp1,temp2,temp3,temp4 = [],[],[],[],[],[],[],[]
    length = int(size/2)
    for i in range(length):
        for j in range(length):
            temp1.append(board[i][j])
            temp2.append(board[i][length+j])
            temp3.append(board[length+i][j])
            temp4.append(board[length+i][length+j])
        arr1.append(temp1)
        arr2.append(temp2)
        arr3.append(temp3)
        arr4.append(temp4)
        temp1,temp2,temp3,temp4 = [],[],[],[]
    
    divide(arr1,length)
    divide(arr2,length)
    divide(arr3,length)
    divide(arr4,length)
    print(')',end='')
    
N = int(input())
board = []
for i in range(N): board.append(list(map(int,input())))
divide(board,N)
