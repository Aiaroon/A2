import random

grid_size = [10,10] #[x,y]
screen_size = [500,500] #[x,y]

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
    

def setup():
    global grid
    grid = get_candy(grid_size)
    size(screen_size[0],screen_size[1])
    strokeWeight(2)

def fillin(grid_x,grid_y,matrix):
   pass
    
def visual(grid_x, grid_y, scr_sizex, scr_sizey, matrix):
    pass

def three_del(grid_x,grid_y,matrix):
    pass

def fall(grid_x,grid_y,matrix):
    pass
    
def mousePressed():
    pass
    
def draw():
    pass
