import pygame
import random

#初始化
pygame.init()
width,height=600,600
cell=20 #单元格的大小
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("贪吃蛇---面试作品")

#颜色定义
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)

#蛇的初始位置(用列表存储坐标)
snake=[(300,300)]
x,y=cell,0 #初始向右移动

#生成第一个食物
def new_food():
    return (random.randint(0,(width//cell)-1)*cell,
            random.randint(0,(height//cell-1)*cell))

food=new_food()

clock=pygame.time.Clock()
score=0
font=pygame.font.Font(None,36)

running=True
while running:
    # 1.事件监听(方向控制)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and y!=cell:
                x,y=0,-cell
            if event.key==pygame.K_DOWN and x!=cell:
                x,y=0,cell
            if event.key==pygame.K_LEFT and x!=cell:
                x,y=-cell,0
            if event.key==pygame.K_RIGHT and x!=-cell:
                x,y=cell,0

    #2.蛇的移动逻辑
    head_x,head_y=snake[0]
    new_head=(head_x+x,head_y+y)
    snake.insert(0,new_head)

    #3.碰撞检测(是否吃到食物)
    if snake[0]==food:
        score+=1
        food=new_food()
    else:
        snake.pop()

    #4.游戏结束判定（撞墙或撞自己)
    if (snake[0][0]<0 or snake[0][0]>=width or snake[0][1]<0 or snake[0][1]>=height):
        running=False
    if snake[0] in snake[1:]:
        running=False

    #5.画面渲染
    screen.fill(black)
    #画蛇
    for segment in snake:
        pygame.draw.rect(screen,green,(segment[0],segment[1],cell,cell))
        #画食物
        pygame.draw.rect(screen,red,(food[0],food[1],cell,cell))
        #画分数
        text=font.render(f"得分:{score}",True,white)
        screen.blit(text,(10,10))
        pygame.display.flip()
        clock.tick(10)
#退出
pygame.quit






