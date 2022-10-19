def add(**vkw):
    print(vkw)
    print(type(vkw))
    for k,v in vkw.items():
        print("{} ----> {}".format(k,v))

#add()
#add(a=66)
add(x=3,y=9,z=6,a=5,b=7) # positional arguments

#dd(55,44,88)