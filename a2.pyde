import random

grid_size = [10,10] #[x,y]
screen_size = [500,500] #[x,y]
grid_per_pixel_y = (screen_size[1] / grid_size[1]) * 2
screen_size_real_y = int(screen_size[1] + grid_per_pixel_y)
score = 0


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
    size(screen_size[0],screen_size_real_y)
    strokeWeight(2)

#===========================================================================
#graphic function
#===========================================================================

def visual(grid_x, grid_y, scr_sizex, scr_sizey, matrix):
    score_grid_step = 50
    score_grid_st = 475
    score_str = str(score)
    inx = len(score_str) -1
    while inx >= 0:
        score_inx = score_str[inx]
        if score_inx == "0":
            zero(score_grid_st,75,30,50)
        if score_inx == "1":
            one(score_grid_st,75,30,50)
        if score_inx == "2":
            two(score_grid_st,75,30,50)
        if score_inx == "3":
            three(score_grid_st,75,30,50)
        if score_inx == "4":
            four(score_grid_st,75,30,50)
        if score_inx == "5":
            five(score_grid_st,75,30,50)
        if score_inx == "6":
            six(score_grid_st,75,30,50)
        if score_inx == "7":
            seven(score_grid_st,75,30,50)
        if score_inx == "8":
            eight(score_grid_st,75,30,50)
        if score_inx == "9":
            nine(score_grid_st,75,30,50)
        score_grid_st = score_grid_st - score_grid_step
        inx = inx - 1
    
    line(0,grid_per_pixel_y,500,grid_per_pixel_y)
    colr = [[255,0,0],[0,255,0],[0,0,255],[255,255,0]]
    stepx = scr_sizex / grid_x
    stepy = scr_sizey / grid_y
    stx = [stepx,stepx/2]
    sty = [stepy,(stepy/2) + grid_per_pixel_y]
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
    fill(150,150,150)
    ellipse(50,50,75,75)
    fill(100,100,100)
    ellipse(150,50,75,75)
    
    
def one(x,y,w,h):
    line(x,y,x,y-h)
    line(x,y-h,x-(w/4),y-(h/2))
def two(x,y,w,h):
    line(x-w,y,x,y)
    line(x-w,y,x,y-(h/1.5))
    line(x,y-(h/1.5),x-(w/2),y - h)
    line(x- (w/2), y - h , x-w , y - (h / 1.5))
def three(x,y,w,h):
    line(x - (w/2),y,x ,y - (h/4) )
    line(x - (w/2),y ,x -w , y - (h/4))
    line(x, y - (h / 4),x - (w / 2) , y - (h / 2))
    line(x - (w / 2) , y - (h / 2) , x, y - (h / 1.5))
    line(x , y - (h / 1.5) , x - (w / 2) , y - h)
    line(x - (w / 2) , y - h , x - w , y - (h / 1.5))
def four(x,y,w,h):
    line(x,y,x,y - h)
    line(x,y - (h / 2) , x - w , y - (h / 2))
    line(x -w , y - (h / 2), x - (w / 1.5) , y - h)
def five(x,y,w,h):
    line(x -w , y - h ,x , y - h)
    line(x -w , y - h , x - w , y - (h / 2))
    line(x - w , y - (h / 2), x - (w / 3), y - (h / 2))
    line(x - (w / 3) , y - (h / 2), x , y - (h / 4))
    line(x , y - (h / 4), x - (w / 3) , y)
    line(x - w , y , x - (w / 3) , y)
def six(x ,y ,w ,h):
    line(x - w , y - (h / 1.25) , x - w , y - (h / 5))
    line(x - w , y - (h / 5) , x - (w / 2) , y )
    line(x - (w / 2) , y , x , y - (h / 3))
    line(x , y - (h / 3) , x - (w / 2) , y - (h / 1.75))
    line(x - (w / 2) , y - (h / 1.75) , x - w , (y - (h / 3)))
    line(x - w , y - (h / 1.25) , x - (w / 2) , y - h)
    line(x - (w / 2) , y - h , x , y - (h / 1.25))
def seven(x,y,w,h):
    line(x , y - h , x - (w / 2) , y)
    line(x , y - h , x - w , y - h)
    line(x - w , y - h , x - (w / 1.25) , y - (h / 1.25))
def eight(x,y,w,h):
    line(x - (w / 1.75) , y - (h / 2) , x - (w / 2.75) , y - (h / 2))
    line(x - (w / 1.75) , y - (h/2) , x - w , y - (h / 1.5))
    line(x - (w / 2.75) , y - (h / 2) , x , y - (h / 1.5))
    line(x - w , y - (h / 1.5) , x - (w / 2) , y - h)
    line(x , y - (h / 1.5) , x - (w/2) , y - h)
    line(x - (w / 1.75) , y - (h/2) , x - w , y - (h / 3.5))
    line(x - (w / 2.75) , y - (h / 2) , x , y - (h / 3.5))
    line(x - w , y - (h / 3.5) , x - (w / 2) , y )
    line(x , y - (h / 3.5) , x - (w/2) , y )
def nine(x,y,w,h):
    line(x , y - h , x - (w / 1.75) , y - h)
    line(x , y - h , x ,y)
    line(x - w , y - (h / 1.75) , x - (w / 1.75) , y - h)
    line(x - w, y - (h / 1.75) , x - (w / 2) , y - (h / 2.5))
    line(x - (w / 2) , y - (h / 2.5) , x ,y - (h / 2))
    line(x , y , x - (w / 1.5), y )
    line(x - (w / 1.5) , y , x -w , y - (h / 3.75))
def zero(x,y,w,h):
    line(x , y ,x - w , y)
    line(x , y ,x , y - h)
    line(x - w ,y - h , x , y - h)
    line(x - w , y - h , x -w  , y)
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
    global score
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
                        score = score + 132
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
        
        
def file_save(grid_x,grid_y,matrix):
    RGB_ = ["R","G","B","Y"]
    saving_grid = []
    y = 0
    while y < grid_y:
        x = 0
        saving_grid_y = []
        matrix_y = matrix[y]
        while x < grid_x:
            saving_grid_y.append(matrix_y[x])
            x = x + 1
        saving_grid.append(saving_grid_y)
        y = y + 1
    y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            colr = saving_grid[y][x] - 1
            saving_grid[y][x] = RGB_[colr]
            x = x + 1
        y = y + 1
    saving_txt = ""
    y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            saving_txt = saving_txt + str(saving_grid[y][x])
            x = x + 1
        saving_txt = saving_txt + "\n"
        y = y + 1
    with open("save.txt","w") as file:
        file.write(saving_txt)
        print(saving_txt)
        
        
def file_load(grid_x,grid_y,matrix):
    with open("save.txt","r") as file:
        lin_e = file.readline()
        matrix1 = []
        while lin_e:
            x = 0
            matrix_y = []
            temp = 0
            txt = ""
            while temp < len(lin_e) - 1:
                    txt = txt + lin_e[temp]
                    temp = temp + 1
            while x < grid_x:
                matrix_y.append(txt[x])
                x = x + 1
            lin_e = file.readline()
            matrix1.append(matrix_y)
    RGB_ = ["R","G","B","Y"]
    y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            inx = matrix1[y][x]
            count = 0
            while count < 4:
                if inx == RGB_[count]:
                    colr_num = count + 1
                    matrix1[y][x] = colr_num
                    count = 4
                count = count + 1
            x = x + 1
        y = y + 1
    y = 0
    while y < grid_y:
        x = 0
        while x < grid_x:
            matrix[y][x] = matrix1[y][x]
            x = x + 1
        y = y + 1
                    
                
            
#===========================================================================
#User interaction
#===========================================================================

def mousePressed():
    save_button = [[1,0],[0,0],[0,1],[1,1]]
    load_button = [[2,0],[3,0],[2,1],[3,2]]
    save_pressed = False
    load_pressed = False
    global selection
    inx = []
    idx = mouseX
    idy = mouseY - grid_per_pixel_y
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
    i = 0
    while i < 4:
        if selection[0] == save_button[i]:
            save_pressed = True
        if selection[0] == load_button[i]:
            load_pressed = True
        i = i + 1
        
    if save_pressed:
        selection = []
        file_save(grid_size[0],grid_size[1],grid)
    if load_pressed:
        selection = []
        file_load(grid_size[0],grid_size[1],grid)
    if len(selection) >= 2:
        x1 = selection[0][0]
        y1 = selection[0][1]
        indx2 = selection[1]
        expected = []
        count = -1
        if selection[1] == selection[0]:
            selection = []
            return
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
    background(255,255,255)
    fillin(grid_size[0],grid_size[1],grid)
    three_del(grid_size[0],grid_size[1],grid)
    fall(grid_size[0],grid_size[1],grid)
    visual(grid_size[0],grid_size[1],screen_size[0],screen_size[1],grid)
