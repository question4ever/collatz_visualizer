from turtle import *

def CollatzConjecture(n):
    if(n>0):
        if(n%2 == 1):
            lt(90)
            fd(10)
            return (3*n + 1)
        elif(n%2 == 0):
            rt(90)
            fd(10)
            return (n/2)

    
def main():
    penup()
    goto(-250,-250)
    pendown()
    v = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 20, 200, 2000, 20000, 200000, 2000000, 20000000,
         40, 400, 4000, 40000, 400000, 4000000, 40000000, 160, 1600, 16000, 160000, 1600000, 16000000, 160000000]
    c = ["red", "blue", "yellow"]
    i = 0
    for n in v:
        if(i > (len(c)-1)):
            i = 0
        color("black", c[i])
        begin_fill()
        while(n > 1):
            n = CollatzConjecture(n)
        end_fill()
        i+=1
    done()


if __name__ == "__main__":
    main()
