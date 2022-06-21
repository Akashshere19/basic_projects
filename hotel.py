class hotelfarecal:
    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=122):
         print("\n\n******WELCOME TO Crown HOTEL****\n")
         self.rt=rt
         self.r=r
         self.t=t
         self.p=p
         self.s=s
         self.a=a
         self.name=name
         self.address=address
         self.cindate=cindate
         self.coutdate=coutdate
         self.rno= rno
         
    def inputdata(self):
        self.name=input("\nEnter your name: ")
        self.address =input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("your room no:",self.rno,"\n")
        
    def roomrent(self):
        print("we have the following rooms are for you:")
        print("1. type A--->rs 6000 PN\-")
        print("2. type B--->rs 5000 PN\-")
        print("3. type C--->rs 4000 PN\-")
        print("4. type D--->rs 3000 PN\-")

        x=int(input("Enter your choice please->"))
        n=int(input("for how many nights did you stay:"))
        if (x==1):
            print("you have opted  room type A")
            self.s=6000*n
            
        elif (x==2):
            print("you have opted  room type A")
            self.s=5000*n
        elif (x==3):
              print("you have opted  room type A")
              self.s=4000*n
        elif (x==4):
            print("you have opted  room type A")
            self.s=3000*n
        else:
            print("Please choose a room")
        print("Your room rent is =",self.s,"\n")

    def restaurentbill(self):
         print("****RESTAURANT MENU****")
         print("1.water ----->Rs20","2.tea---->Rs.10","3.breakfast combo--->Rs.90","4.lunch---->Rs.110","5.dinner---->Rs.150","6.Exit")

         while (1):
              c= int(input("Enter your choice:"))
              if (c ==1):
                  d=int(input("Enter the quantity:"))
                  self.r=self.r+20*d
              elif (c ==2):
                  d=int(input("Enter the quantity:"))
                  self.r=self.r+10*d
              elif (c==3):
                    
                  d=int(input("Enter the quantity:"))
                  self.r=self.r+90*d
              elif (c ==4):
                  d=int(input("Enter the quantity:"))
                  self.r=self.r+110*d
              elif (c ==1):
                  d=int(input("Enter the quantity:"))
                  self.r=self.r+150*d

              elif (c==6):
                  break
                
              else:
                  print("Invalid Option")
              print("Total food Cost =Rs",self.r,"\n")
          
     
    def laundrybill(self):
         print("****LAUNDRY MENU****")
         print("1.Shorts ----->Rs.3","2.Trousers---->Rs.4","3.Shirt--->Rs.5","4.jeans---->Rs.8","5.Girlsuit---->Rs.10","6.Exit")

         while (1):
              e= int(input("Enter your choice:"))
              if (e ==1):
                  f=int(input("Enter the quantity:"))
                  self.t=self.t+3*f
              elif (e ==2):
                  f=int(input("Enter the quantity:"))
                  self.t=self.t+4*f
              elif (e==3):
                  f=int(input("Enter the quantity:"))
                  self.t=self.t+5*f
              elif (e ==4):
                  f=int(input("Enter the quantity:"))
                  self.t=self.t+8*f
              elif (e ==5):
                  f=int(input("Enter the quantity:"))
                  self.t=self.t+10*d

              elif (e==6):
                  break
                
              else:
                  print("Invalid Option")
              print("Total Laundry Cost =Rs",self.t,"\n")

    def gamebill(self):
         print("****Game MENU****")
         print("1.Table tennis>Rs.30","2.Bowling---->Rs.40","3.Snooker--->Rs.50","4.Video Game---->Rs.80","5.Pool---->Rs.100","6.Exit")

         while (1):
              g= int(input("Enter your choice:"))
              if (g ==1):
                  h=int(input("Enter the quantity:"))
                  self.p=self.p+60*h
              elif (g ==2):
                  h=int(input("Enter the quantity:"))
                  self.p=self.p+80*h
              elif (g==3):
                  h=int(input("Enter the quantity:"))
                  self.p=self.p+70*h
              elif (g ==4):
                  h=int(input("Enter the quantity:"))
                  self.p=self.p+90*h
              elif (g ==5):
                  h=int(input("Enter the quantity:"))
                  self.p=self.p+50*h

              elif (g==6):
                  break
                
              else:
                  print("Invalid Option")
              print("Total Laundry Cost =Rs",self.p,"\n")
    def display(self):
         print("******HOTEL BILL******")
         print("Customer details:")
         print("Customer name:",self.name)
         print("Customer address:",self.address)
         print("Check in date:",self.cindate)
         print("Check out date:",self.coutdate)
         print("Room no:",self.rno)
         print("Your Room Rent is:",self.s)
         print("Your Food bill is:",self.r)
         print("Your Laundry bill is:",self.t)
         print("Your Game bill is:",self.p)
         self.rt=self.s+self.t+self.p+self.r
         print("Your sub total bill is :",self.rt)
         print("Additional Service Charges is",self.a)
         print("Your grad total bill is:",self.rt+self.a,"\n")
         self.rno+=1

def main():
    a=hotelfarecal()

    while(1):
        print("1.Enter Customer Data")
        print("2.Calculate roomrent")
        print("3.Calculate restaurant bill")
        print("4.Calculate laundry bill")
        print("5.Calculate game bill")
        print("6.show total cost")
        print("7.Exit")
        b=int(input("\nEnter your choice :"))
        if (b==1):
            a.inputdata()
        if (b==2):
            a.roomrent()
        if (b==3):
            a.restaurentbill()
        if (b==4):
            a.laundrybill()
        if (b==5):
            a.gamebill()
        if (b==6):
            a.display()
        if (b==7):
            quit()    

main()

              
