def y(x):
    return x**3
def turev(x):
    return 3*x**2
def forward(x,h):
    fd= (y(x+h)-y(x))/h
    error=(turev(x)-fd)
    print("forwad=\n",fd,"\nhata=\n",error)

forward(1,0.2)
forward(1,0.1)
def central(x,h):
    cd=(y(x+h)-y(x-h))/(2*h)
    error=(turev(x)-cd)
    print("central=\n",cd,"\nhata=\n",error)


central(1,0.2)
central(1,0.1)
def backwards(x,h):
    bw=(y(x)-y(x-h))/h
    error=(turev(x)-bw)
    print("backwards=\n",bw,"\nhata=\n",error)

backwards(1,0.2)
backwards(1,0.1)




