import random

grid_size = [10,10] #[x,y]
screen_size = [500,500] #[x,y]

#===========================================================================
#setup
#===========================================================================

def get_candy(grid_size):
    grid = []
    i = 0
    #leave 3 space right and below so we don't have to deal with index out of range
    while i < grid_size[1]+3:
        grid_y = []
        j = 0
        while j < grid_size[0]+3:
            grid_y.append(0)
            j = j + 1
        i = i + 1
        grid.append(grid_y)
    return grid
    
#---------------------------------------------------------------------------

def setup():
    global grid
    grid = get_candy(grid_size)
    size(screen_size[0],screen_size[1])
    strokeWeight(2)

#===========================================================================
#graphic function
#===========================================================================

def visual(grid_x, grid_y, scr_sizex, scr_sizey, matrix):
    pass

#===========================================================================
#backend fuction
#===========================================================================

def fillin(grid_x,grid_y,matrix):
   y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            if matrix[y][x] == 0:
                matrix[y][x] = random.randint(1,4)
            x = x + 1
        y = y + 1
    
#---------------------------------------------------------------------------

def three_del(grid_x,grid_y,matrix):
    y = 0
    did_del = False
    while y < grid_y:
        x = 0
        while x < grid_x:
            reach = 1
            spc = matrix[y][x]
            delable_x = True
            delable_y = True
            while reach < 3:
                if spc != matrix[y][x + reach]:
                    delable_x = False
                if spc != matrix[y + reach][x]:
                    delable_y = False
                reach = reach + 1
            reach = 0
            if delable_x:
                while reach < 3:
                    matrix[y][x + reach] = 0
                    reach = reach + 1
                did_del = True
            else:
                if delable_y:
                        while reach < 3:
                            matrix[y + reach][x] = 0
                            reach = reach + 1
                        did_del = True
            if did_del:
                return
            x = x + 1
        y = y + 1

#---------------------------------------------------------------------------

def fall(grid_x,grid_y,matrix):
    pass

#===========================================================================
#User interaction
#===========================================================================

def mousePressed():
    pass
    
#===========================================================================
#main
#===========================================================================

def draw():
    pass
