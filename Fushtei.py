import math
def angle(Ex, Ey):  #визначаємо кут повороту
    kpl=math.sqrt((Ex-Ax)**2+(Ey-Ay)**2)
    kpr=math.sqrt((Dx-Ex)**2+(Dy-Ey)**2)
    gip=math.sqrt(kpl**2+kpr**2)
    cosfA=kpl/gip
    sinfA=kpr/gip
    return cosfA, sinfA
Ax, Ay, Cx, Cy = map(float, input('vvedit koordynaty protylejnych vershyn kvadrata Ax, Ay, Cx, Cy').split())

if Ax==Cx and Ay==Cy:
    print("vasha figura ne kvadrat")
else:
    Sx, Sy, = map(float, input('vvedit koordynaty tochky Sx, Sy').split())

    Ox=(Ax+Cx)/2 #шукаємо координати точок В і D
    Oy=(Ay+Cy)/2

    AOx=Ox-Ax
    AOy=Oy-Ay

    ODx=AOy       
    ODy=-AOx

    OBx=-AOy
    OBy=AOx

    Dx=ODx+Ox
    Dy=ODy+Oy

    Bx=OBx+Ox
    By=OBy+Oy
  
    Axc=Ax-Ax # переносимо центр координат в точку А і визначаємо нові координати точок
    Ayc=Ay-Ay

    Bxc=Bx-Ax
    Byc=By-Ay

    Cxc=Cx-Ax
    Cyc=Cy-Ay

    Sxc=Sx-Ax
    Syc=Sy-Ay

    if Bxc>=0 and Byc>=0: # визначаємо кут повороту в залежності від чверті
        Ex=Ax
        Ey=Dy
        cosA, sinA=angle(Ex, Ey)
        cos1A=sinA
        sin1A=-cosA
#        print("1")
    if Bxc<=0 and Byc>=0:
        Ex=Dx
        Ey=Ay
        cosA, sinA=angle(Ex, Ey)
        cos1A=cosA
        sin1A=sinA
#        print("2")
    if Bxc<=0 and Byc<=0:
        Ex=Ax
        Ey=Dy
        cosA, sinA=angle(Ex, Ey)
        cos1A=-sinA
        sin1A=cosA
#        print("3")
    if Bxc>=0 and Byc<=0:
        Ex=Dx
        Ey=Ay
        cosA, sinA=angle(Ex, Ey)
        cos1A=-cosA
        sin1A=-sinA
#        print("4")

     
    Cx1=Cxc*cos1A+Cyc*sin1A #повертаємо систему координат і визначаємо нові координати
    Cy1=-Cxc*sin1A+Cyc*cos1A

    Sx1=Sxc*cos1A+Syc*sin1A
    Sy1=-Sxc*sin1A+Syc*cos1A
    
    if 0<=Sx1 and Sx1<=Cx1 and 0<=Sy1 and Sy1<=Cy1:
        print('YES')
    else:
        print('NO')





