import pandas as pd
import numpy as np
import sympy as sy
import scipy as sp

# 引入正态分布
from scipy.stats import norm


# 声明符号变量
x = sy.symbols('x')
y = sy.symbols('y')
z = sy.symbols('z')
u = sy.symbols('u')
lamd = sy.symbols('lambda')
mu = sy.symbols('mu')
theta = sy.symbols('theta')
sigma = sy.symbols('sigma')
r = sy.symbols('r', nonnegative=True)

def calc_C(n,m):
    a = sy.factorial(n)
    b = sy.factorial(m) * sy.factorial(n-m)
    return a/b

def normal_distributes(mu,sigma,symbols = 'x'):
    x = sy.symbols(symbols)
    func_normal_dist = (1/(sy.sqrt(2*sy.pi)*sigma)) * sy.exp(-((x-mu)**2/(2*(sigma**2))))
    return func_normal_dist


# practise_5
x = sy.symbols('x')
y = sy.symbols('y')

f_xy = 4.8*y*(2-x)

f_x = sy.integrate(f_xy,(y,0,x))
f_y = sy.integrate(f_xy,(x,y,1))

# practise 6
f_xy = sy.exp(-y)
f_x = sy.integrate(f_xy,(y,x,sy.oo))
f_y = sy.integrate(f_xy,(x,0,y))

# practise 7
f_xy = x**2*y
c_rever = sy.integrate(f_xy,(y,x**2,1),(x,-1,1))
c_ = 1/c_rever
f_xy = c_* x**2*y

f_x = sy.integrate(f_xy,(y,x**2,1))

f_y = sy.integrate(f_xy,(x,-sy.sqrt(y),sy.sqrt(y)))
# practise_11——1
f_xy_y = f_xy/f_y
f_xy_y.evalf(subs={'y':1/2})

# practise_11——2
f_xy_y = f_xy/f_y
f_xy_y.evalf(subs={'y':1/2})

f_xy_x = f_xy/f_x
f_xy_x.evalf(subs={'y':1/3,'x':1/2})

# practise_11——3
'''
由已知
x**2<y<1
'''
A = f_xy_x.evalf(subs={'x':1/2})
ans_11_3_1 = sy.integrate(A,(y,1/4,1))
ans_11_3_2 = sy.integrate(A,(y,3/4,1))

'''
条件概率 : f(x|y) = f(x,y)/f(y)
'''

# 9
n = sy.symbols('n')
m = sy.symbols('m')
#
f_xy = sy.exp(-14)* 7.14**(m) * 6.86**(n - m) /( sy.factorial(m) *sy.factorial(n-m))
'''
提出:sy.exp(-14) ,上下同乘 n!
 = (sy.exp(-14)/sy.factorial(n) ) * (sy.factorial(n) * (7.14**(m) * 6.86**(n - m)) /( sy.factorial(m) *sy.factorial(n-m)))
二项式展开后
=sy.exp(-14)/sy.factorial(n)* (7.14 + 6.86)**(n)
'''
f_x =  sy.exp(-14)/sy.factorial(n)* (7.14 + 6.86)**(n)

'''
P{Y=m} = SUM[m,n]P{X=n,Y=m}
= sy.exp(-14)/sy.fatorial(m) *(7.14)**m   * SUM[m,oo]
'''

f_y_1 = sy.exp(-14)/sy.factorial(m) *(7.14)**m

f_y_2 = (6.86)**(n-m) / sy.factorial(n-m)
f_y_2 = sy.summation(f_y_2,(n,m,sy.oo))

# 对f_y_2变形
'''
令  k = n-m,
则f_y_2变形为
sy.summation(6.86**k/sy.factorial(k),k,(k,0,sy.oo))
'''
k = sy.symbols('k')
f_y_2 = sy.summation(6.86**k/sy.factorial(k),(k,0,sy.oo))
print(f_y_2)
f_y_2 = sy.exp(1)**6.86
f_y  = f_y_1 * f_y_2



# practise_12
f_xy = 1
f_x = sy.integrate(f_xy,(y,-x,-x))

# 下半部分
f_y_1 = sy.integrate(f_xy,(x,-y,1))

# 上半部分
f_y_2 = sy.integrate(f_xy,(x,y,1))

f_xy_x_1 = f_xy


# 第四章 12题
'''

'''
f_xy = 1
x =sy.symbols('x')
y = sy.symbols('y')
f_X = sy.integrate(f_xy,(y,-x,x))

# 分类讨论,因为上下不同
f_Y_up = sy.integrate(f_xy,(x,y,1))
f_Y_down = sy.integrate(f_xy,(x,-y,1))

# 14
'''
X是为1的均匀分布，且两者互相独立,相乘即可
确定了计算的域
x{0,1} ,y>0
'''
x = sy.symbols('x')
y = sy.symbols('y')
f_Y = (1/2)*sy.exp(-y/2)
f_X = 1
f_xy = f_Y*f_X
#

integrate_y_14 = sy.integrate(f_xy,(y,0,x**2))
# 对于exp(-x^2/2),转换为正态分布函数求Fi即可
answer_14 = 1 - np.sqrt(2)*sy.pi*(norm.cdf(1) - norm.cdf(0))

# asnwer_15
'''
由题已知 X,Y的概率密度分布为1/sy.sqrt(2*sy.pi)
'''
def get_yacobian_matix(target_vari_list,transform_vari_list):
    funcs = sy.Matrix(target_vari_list)
    args = sy.Matrix(transform_vari_list)
    res = funcs.jacobian(args)
    return res

func_x = normal_distributes(0,1,symbols = 'x')
func_y = normal_distributes(0,1,symbols = 'y')
f_xy = (func_x * func_y).simplify()

theta = sy.symbols('theta')
r = sy.symbols('r', nonnegative=True)
x_polar = r*sy.cos(theta)
y_polar = r*sy.sin(theta)
polar_fxy = f_xy.subs(((x, x_polar), (y, y_polar))).simplify()
polar_fxy = sy.integrate(polar_fxy,(theta,0,2*sy.pi))

# 雅可比行列式对dxdy进行函数变换之后 补上|det(jacobian)|
jacobi_dxdy = get_yacobian_matix([x_polar,y_polar],[r,theta])

polar_r_theta = polar_fxy * jacobi_dxdy.det().simplify()

# 根据题目给出的要计算出的范围算出值
F_D1 = sy.integrate(polar_r_theta,(r,0,1))
F_D2 = sy.integrate(polar_r_theta,(r,1,2))
F_D3 = 1 - F_D1 - F_D2

# answer_16
lamd = sy.symbols('lambda')
mu = sy.symbols('mu')
f_X = lamd * sy.exp(-lamd*x)
f_Y = mu * sy.exp(-mu*y)

# 对应独立条件概率,
# 第一问的结果直接就 f_X

'''
对于X>Y和X<=Y,有不同的情况
'''
f_xy = f_X*f_Y

# 针对X<=Y
'''
因为sy算无穷大的积分算出来不行我就手算了
'''
F_1 = lamd/(lamd+mu)

# X>Y的概率等于 1 - P{X<Y}
F_2 = (1 - F_1).simplify()

# Z的分布律
Z = {'0':F_1,
     '1':F_2}

# Z的分布函数(求累计)
Z = {'z<0':0,
    '0<=z<1':F_1,
    'z>=1':F_1+F_2}

# 3.answer_17 #
f_x = 1
f_y = sy.exp(-y)
# 求Z=X+Y
f_xy = f_x*f_y
# 解法1
# 针对线性变量组合使用的卷积公式

'''
卷积公式有两点:
    1、
    2、
'''

# 我自己这里的思路是解法2的思路
'''
这里要讨论Z数值的大小
x
|        /|
|       /||
|      /|||
|     /||||
|    /|||||
|   /||||||
|  /|||||||
|_/||||||||____________x

1、如果Z小于0,在x,y的值域之外
2、如果Z小于1,x的右侧上限为Z
3、如果Z大于1,X的右侧上限为1
'''
z = sy.symbols('z')
F_1 = 0
F_2 = sy.integrate(f_xy,(y,0,z-x),(x,0,z))
F_3 = sy.integrate(f_xy,(y,0,z-x),(x,0,1))
f_2,f_3 = F_2.diff(z),F_3.diff(z)

# 3.answer_18
'''
二维随机变量用卷积公式
f_t  = t*exp(-t)
令Z = X1+X2

由卷积公式
f(z) = ∫[-oo,+oo]f(z)f(z-x)dx
由f(t)的定义,只有t>0时原函数才有意义

∴{x>0,z-x>0}
    => {x>0,x<z}

y
|        /|
|       /||
|      /|||
|     /||||
|    /|||||
|   /||||||
|  /|||||||
|_/||||||||_______________x
'''


fz = x*sy.exp(-x) * (z-x)*sy.exp(-(z-x))

F_z = sy.integrate(fz,(x,0,z))

'''
同理对W =  Z+X3(仍然是互相两两独立)
卷积公式的拓展
'''
f_t  = x*sy.exp(-x)

F_u_z = f_t.evalf(subs={'x':u-x}).simplify()

f_uz = F_z.evalf(subs={'z': x}) * F_u_z

F_w = sy.integrate(f_uz,(x,0,u))

'''
19 题
'''
f_xy = 1/2 *(x+y)*sy.exp(-(x+y))

# 证独立
# 因为x,y在小于等于0的区域无意义

F_x = sy.integrate(f_xy,(y,0,+sy.oo))

# 因为两个随机变量乘积不为FXY, 不独立
F_xy = F_x * F_x.evalf(subs={'x':y}).simplify()

'''
由定义,
X>0,Y>0
>=
Z-Y >0,Y >0

变成了
y<z
y>0

y        y=z
|        /|
|       /||
|      /|||
|     /||||
|    /|||||
|   /||||||
|  /|||||||
|_/||||||||_______________z
'''
f_xy  = 1/2*(x+y)*sy.exp(-(x+y))
f_z = f_xy.evalf(subs={'x':z-y,}).simplify()
F_z = sy.integrate(f_z,(y,0,z))

# 20
f_z  = z/sigma**2 * sy.exp( - (z**2/2/sigma**2))

# 因为x,y相互独立
'''
F(x,y) = F(X) * F(Y)
P{Z <= z}
P{sqrt(x**2+y**2) <= z}
# 由正态分布定义,Z <- 0 时，F(z) = 0
只考虑 Z> 0 的情况
'''

f_xy = normal_distributes(0,sigma,symbols = 'x') * normal_distributes(0,sigma,symbols = 'y')
f_xy = f_xy.simplify()

# 转换极坐标
x_polar = r*sy.cos(theta)
y_polar = r*sy.sin(theta)
jacobi_dxdy = get_yacobian_matix([x_polar,y_polar],[r,theta]).det().simplify()
polar_fxy_no_d = f_xy.subs(((x, x_polar), (y, y_polar))).simplify()
polar_fxy = polar_fxy_no_d * jacobi_dxdy
#
polar_Fxy = sy.integrate(polar_fxy,(r,0,z))  * (2*sy.pi)
polar_Fxy = polar_Fxy.simplify()

f_z  = polar_Fxy.diff(z)


# ------------------ 21 ------------------ #
f_xy_k = sy.exp(-(x+y))
F_xy_k = sy.integrate(f_xy_k,(x,0,1),(y,0,sy.oo))
k = 1/F_xy_k

f_xy = k * f_xy_k

f_x = sy.integrate(f_xy,(y,0,sy.oo)).simplify()
f_y = sy.integrate(f_xy,(x,0,1)).simplify()


# 针对U = MAX(X,Y)
'''
P{U < z}
因为相互独立
P{X<= Z,Y<= Z}
P{X}* P{Y}

边缘分布已经算出
'''
# 因为X属于0~1
F_x = sy.integrate(f_x,(x,0,u)).simplify()

F_y = sy.integrate(f_y,(y,0,u)).simplify()



# 小于0时为0
F_U = 0

# 0到1时
F_U =  F_x *F_y

# 大于1时
F_U = 1 -sy.exp(-u)

# ----- 22 ------ #
X_i = norm(160,20)

p = X_i.cdf(180)
res_22 = (1-p)**4

# -------------------- 23 --------------------- #
# 写出瑞利分布
f_z  = z/sigma**2 * sy.exp( - (z**2/2/sigma**2))
f_z = f_z.evalf(subs = {sigma:2})

raily_distri =  sy.integrate(f_z,(z,0,x)).simplify()

# 如果他们是独立同分布
# 1) Z = max{X1,X2,X3,X4,X5}
# Z = X1* .... * X5
F_z = raily_distri**5

# P{Z > 4} >= 1 - P{Z<= 4}
# 1 - F(4)
res_23 = 1 - F_z.evalf(subs = {x:4})

# -------------------- 24 --------------------- #

# 参考教材P99
'''
不妨令X,Y的分布函数为F(z)
'''
# N = min(X,Y)
# Fn = 1 = [1-F(z)]^2
# P{a < N <b} < = Fn(b) - Fn(a)
# [1-F(a)]^2 - [1 - F(b)]^2

