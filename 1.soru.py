import  math
def y(x):
    return math.e**x                                             

def forward(x,h):
    fd= (y(x+h)-y(x))/h

    print("forwad=\n",fd)

forward(1,0.2)

def central(x,h):
    cd=(y(x+h)-y(x-h))/(2*h)

    print("central=\n",cd)


central(1,0.2)

def backwards(x,h):
    bw=(y(x)-y(x-h))/h

    print("backwards=\n",bw)

backwards(1,0.2)





