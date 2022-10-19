def myfun(a,b,*vrg,c=0,d=0,**kvrg):
    print("POSITIONAL")
    print("a=",a,"b=",b,"c=",c,"d=",d)
    print("DEFAULT")
    print("c=", c, "d=", d)
    print("variable")
    print(vrg)
    print('KEYWORD VARIABLE')
    print(kvrg)

#myfun(76,34) # actual arguments
#myfun(7,3,9,8)# actual  arguments
#myfun(3,5,7,9,11,22,33,44,55,x=100,y=500,z=900) # actual arguments and positional arguments
myfun(3,5,7,9,11,22,33,44,55,c=54,d=98,x=100,y=500,z= 900) #

#myfun(5,8)