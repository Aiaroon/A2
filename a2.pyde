import random

grid_size = [10,10] #[x,y]
screen_size = [500,500] #[x,y]

selection = []

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
    colr = [[255,0,0],[0,255,0],[0,0,255],[255,255,0]]
    stepx = scr_sizex / grid_x
    stepy = scr_sizey / grid_y
    stx = [stepx,stepx/2]
    sty = [stepy,stepy/2]
    radius_x = stx[0] - 10
    radius_y = sty[0] - 10
    y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            idx = matrix[y][x]
            R = colr[idx-1][0]
            G = colr[idx-1][1]
            B = colr[idx-1][2]
            x_D = (x * stx[0]) + stx[1]
            y_D = (y * sty[0]) + sty[1]
            if idx > 0:
                fill(R,G,B)
            else:
                fill(0,0,0)
            ellipse(x_D,y_D,radius_x,radius_y)
            
            x = x + 1
        y = y + 1

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
            x = x + 1
        y = y + 1
    return did_del

#---------------------------------------------------------------------------

def fall(grid_x,grid_y,matrix):
    y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            if matrix[y][x] == 0:
                y_cut = 0
                stack = []
                while y_cut < y:
                    stack.append(matrix[y_cut][x])
                    matrix[y_cut][x] = 0
                    y_cut = y_cut + 1
                y_cut = 1
                while y_cut < y + 1:
                    matrix[y_cut][x] = stack[y_cut-1]
                    y_cut = y_cut + 1
            x = x + 1
        y = y + 1

#===========================================================================
#User interaction
#===========================================================================

def mousePressed():
    global selection
    inx = []
    idx = mouseX
    idy = mouseY
    stepx = screen_size[0] / grid_size[0]
    stepy = screen_size[1] / grid_size[1]
    countx = 1
    county = 1
    x = 0
    y = 0
    
    while countx < grid_size[0]+1:
        x = countx * stepx
        if x > idx:
            inx.append(countx - 1)
            countx = grid_size[0]
        countx = countx + 1
    while county < grid_size[1] + 1:
        y = county * stepy
        if y > idy:
            inx.append(county - 1)
            county = grid_size[1]
        county = county + 1
    selection.append(inx)
    print(selection)
    
    if len(selection) >= 2:
        x1 = selection[0][0]
        y1 = selection[0][1]
        indx2 = selection[1]
        expected = []
        count = -1
        while count < 2:
            expected.append([x1 + count,y1])
            expected.append([x1,y1 + count])
            count = count + 2
        count = 0
        while count < 4:
            if indx2 == expected[count]:
                x2 = indx2[0]
                y2 = indx2[1]
                temp = grid[y1][x1]
                grid[y1][x1] = grid[y2][x2]
                grid[y2][x2] = temp
            count = count + 1
        if three_del(grid_size[0],grid_size[1],grid):
            return
        else:
            temp = grid[y1][x1]
            grid[y1][x1] = grid[y2][x2]
            grid[y2][x2] = temp
        selection = []
    
#===========================================================================
#main
#===========================================================================

def draw():
    background(50,50,50)
    fillin(grid_size[0],grid_size[1],grid)
    three_del(grid_size[0],grid_size[1],grid)
    fall(grid_size[0],grid_size[1],grid)
    visual(grid_size[0],grid_size[1],screen_size[0],screen_size[1],grid)
