from pymodbus.client.sync import ModbusTcpClient
import socket
import urllib.request, json
import requests
import pyodbc
from mysql.connector import errorcode
import time
import schedule
from datetime import date
from datetime import datetime
import traceback
import threading
list1=[]
mclist={"RBN01": 10,
                "RBN02": 8,
                "RBN03": 6,
                "RBNH01": 4,
                "RBN05": 2,
                "RBN06": 0
            }
mcstatus={"RBN01": 0,
                "RBN02": 0,
                "RBN03": 0,
                "RBNH01": 0,
                "RBN05": 0,
                "RBN06": 0
            }
final_list=[]

#PROD
base_url = "http://192.168.8.30/RDMS_PROD/"
#TEST
#test_url = "http://192.168.8.253/RDMS_TEST/"

def start():
    try:
        for k in mclist:
            global client1
            client1 = ModbusTcpClient('192.168.8.190',port=502) 
            print(k + " :: " + str(mclist[k]))
            res = client1.read_holding_registers(address=mclist[k],unit=1,count=2)
            #res = client1.read_holding_registers(address= 0x003, unit=1,count=2)
            ptn=res.registers[0]
            mcstatus[k] = ptn
            print("PTN  :: {0}".format(ptn))
            #if end=1 collect and put on url ///end=2 collect ,put on url  and put end time,end date on url
            if ptn==1 or ptn==9:
                try:
                    process1(k, mclist[k])
                except:
                    pass
            else:
                time.sleep(1)
            #print("change ptn to 1")
            #time.sleep(1)
            
    except Exception as e:
        traceback.print_exc()       
   
        

def process1(mc, address):
   
  
    s = socket.socket()
   
    url = base_url + "public/index.php/production/"
    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 7051

    # cnx = mysql.connector.connect(user='root', password='root',host='localhost',                           database='resibon')
    # cnx = mysql.connector.connect(option_files='C:/Users/User/Documents/resibon.mwb')
    s.bind(('', port))
    
    # put the socket into listening mode
    s.listen(5)
   
    ######url1############
    complete_url1 = url + 'get_loaded_furnaces?CCN=DRT&WC=R-BAKE'

   
    #list1 = process(complete_url1)
    complete_url2 = url + 'get_furnace_data?CCN=DRT&ML=ROJ&FURNACE_NUM=%s' % (mc)
    Insert_PTN_DB_data(complete_url2, address, mc)
    


def process(complete_url):
    url1 = complete_url
    print(url1)
    r = requests.get(url1)
    data = (r.json())

    for element in data["MACHINE_LIST"]:
       
        list1.append(element["MACHINE_NUM"])
    #         for x in data["MACHINE_NUM"]

    return list1

def Insert_PTN_DB_data(complete_url2, address, mc):
   
    r1 = requests.get(complete_url2)
    data = (r1.json())
    
    mess_id = data["MESSAGE_ID"]
    
    startdate12=data["START_DATE"]
    starttime12=data["START_TIME"]
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    
    starttime = dt_string
    machineNo = data["FURNACE_NO"]
    PTN = data['PTN']
    datenow = data['START_DATE']
    MAS_LOC = data['MAS_LOC']
    START_DATE = datetime.strptime(datenow, '%d-%m-%Y')
    now = datetime.now().date()
    startdate = datetime.today().strftime('%m/%d/%Y')
    startdate=str(startdate)


   # jsondata = {"MESSAGE_ID": mess_id, "START_TIME": dt_string, "TEMPERATURE_LIST": [], "END_DATE": "","START_DATE":startdate12,
                #"END_TIME": "", "return_val": True}
    global jsondata
    jsondata={"END_DATE": "","END_TIME": "","FURNACE_NO":machineNo,"MACHINE_DESC":"","MACHINE_LIST":"",
              "MAS_LOC":MAS_LOC,"MESSAGE_ID": mess_id,"PTN":PTN,"START_DATE":startdate12, "START_TIME": starttime12, 
              "TEMPERATURE_LIST": [],"return_val": True}
        
    global endjsondata
  #  endjsondata = {"MESSAGE_ID": mess_id, "END_DATE": "", "END_TIME": "","START_TIME": dt_string,"START_DATE":startdate12,
            #       "return_val": True}
    endjsondata={"END_DATE": "","END_TIME": "","FURNACE_NO":machineNo,"MACHINE_DESC":"","MACHINE_LIST":"","MAS_LOC":MAS_LOC,"MESSAGE_ID": mess_id,"PTN":PTN,"START_DATE":startdate12, "START_TIME": dt_string,"return_val": True}

#     try:
#         temp = data['TEMPERATURE_LIST']
#         for td in temp:
#             print(td['SEQ'])
#             query1 = "INSERT INTO [db_resibon].[dbo].[{0}] (machine,sequence,temperature_time,step_number,KP_SV,KP_PV,DB_SV,DB_PV, OXY_ACT, OXY_STD) VALUES (?,?,?,?,?,?,?,?,?,?)".format(mc)
#             today = date.today()
#             print(query1) 
#             machineno = machineNo
#             now = datetime.now()
#             dt_string = now.strftime("%H:%M:%S")
#              
#       
#             data_employee = (machineno,td['SEQ'],dt_string,td['STEP_NO'],td['KP_SV'],td['KP_PV'],td['DB1_SV'],
#                              td['DB1_PV'], td['OXY_ACT'], td['OXY_STD'])
#             pnx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                           "Server=THAIPLC\MSSQLRESIBON;"
#                           "Database=db_resibon;"
#                           "Trusted_Connection=yes;")
#             cursor = pnx.cursor()
#             cursor.execute(query1, data_employee)
#             pnx.commit()
#         pnx.close()
#     except Exception as e:
#         print("Database Exception  - 1")
#         print(e)
        
  

    try:
        query1 = "INSERT INTO [db_resibon].[dbo].[data] (machine_no,message_id,mas_loc, ptn,start_date,start_time,date) VALUES (?,?,?,?,?,?,?)"
        data_employee = (machineNo, mess_id, MAS_LOC, PTN, START_DATE, starttime, now)
        pnx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                             "Server=THAIPLC\MSSQLRESIBON;"
                             "Database=db_resibon;"
                             "Trusted_Connection=yes;")
        cursor = pnx.cursor()
        cursor.execute(query1, data_employee)
        pnx.commit()
        pnx.close()
    except Exception as e:
        print("Database exception")
        print(e)
    
    checkfordataput(machineNo, address)
    
    
def checkfordataput(machineNo, address):
    res = client1.read_holding_registers(address=address, unit=1,count=2)
    #res = client1.read_holding_registers(address=0x004, unit=1,count=2)
    ptn=res.registers[0]
    print("checkforupdate ptn is",ptn)
    #if end=1 collect and put on url ///end=2 collect ,put on url  and put end time,end date on urlS
    
    if (ptn==1 or ptn==9):
        putdata(machineNo, address)
    else:
        time.sleep(2)
#             checkfordataput()
           
def putdata(machineNo, address):
    try:
        res = client1.read_holding_registers(address=address, unit=1,count=2)
        #res = client1.read_holding_registers(address=0x004, unit=1,count=2)
       
        END_NO=res.registers[1]
        print("END_NO : {0}".format(END_NO))
        #if end=1 collect and put on url ///end=2 collect ,put on url  and put end time,end date on url
        if __name__=='__main__':
            th = threading.Thread(target=checkfordataput)
            th.start()       
        if (END_NO==1 ):
            putonurl(machineNo)
            time.sleep(1)
        elif(END_NO==2 ):
            client1.close()
            mcstatus[machineNo] = 0
            putonurlandendime(machineNo)
        else:
            time.sleep(1)
#                 putdata()
         
    except Exception as e:
        print("Putdata exception")
        print(e)
           
#         putdata()         
        


        
def putonurl(machineNo):
    print("START PUTONURL")
    complete_url3= base_url + 'public/index.php/production/save_furnace_sheet?'
    try:
            query1 = "select * from [db_resibon].[dbo].[{0}] ORDER BY id DESC".format(machineNo)
            pnx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=THAIPLC\MSSQLRESIBON;"
                          "Database=db_resibon;"
                          "Trusted_Connection=yes;")
            cursor = pnx.cursor()
            cursor.execute(query1)
            data=(cursor.fetchone())
            pnx.commit()
            pnx.close()
            now = data[15]
            dt_string = now.strftime("%H:%M:%S")
            seq='{0:04}'.format(data[1])
            #seq='{0}'.format(data[1])
            oxystd = ""
            oxyact = 0.0
            if jsondata['PTN'] == "PTN-5":
                oxystd = data[14]
                oxyact = data[13]
            
            if data[1] == 1:
                dict1 ={"DB1_PV":data[7],"DB1_SV":data[6],"DB2_PV":"","DB2_SV":"","KP_PV":data[5],"KP_SV":data[4],
                        "OXY_ACT":float("{:.3f}".format(oxyact)),"OXY_STD":oxystd,"SEQ":seq,"STEP_NO":data[3],"TIME":dt_string, "START_TIME": dt_string}
            else:
                dict1 ={"DB1_PV":data[7],"DB1_SV":data[6],"DB2_PV":"","DB2_SV":"","KP_PV":data[5],"KP_SV":data[4],
                        "OXY_ACT":float("{:.3f}".format(oxyact)),"OXY_STD":oxystd,"SEQ":seq,"STEP_NO":data[3],"TIME":dt_string}
            stepno=data[3]
            jsondata["TEMPERATURE_LIST"].append(dict1)
            if data[1] == 1:
                jsondata['START_TIME'] = dt_string
            
            
            jsondata1=json.dumps(jsondata)
            print(jsondata1)
            
            headers= {
            "Accept": "application/json",
            "Content-Type": "application/json"
               }
            
            
            print(complete_url3)
            r=requests.put(complete_url3,data={"data":jsondata1},headers=headers)
            
            print(r.content)
            print(r.status_code,stepno)
            time.sleep(1)
    
#             putdata()
    except Exception as e:
        print (e)       
    print("END PUTONURL")
    
def  putonurlandendime(machineNo):
    print("START URLEND")
    complete_url3= base_url + 'public/index.php/production/save_furnace_sheet?'
    try:
            query1 = "select * from [db_resibon].[dbo].[{0}] ORDER BY id DESC".format(machineNo)
            pnx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=THAIPLC\MSSQLRESIBON;"
                          "Database=db_resibon;"
                          "Trusted_Connection=yes;")
            cursor = pnx.cursor()
            cursor.execute(query1)
            data=(cursor.fetchone())
            pnx.commit()
            pnx.close()
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            seq='{0:04}'.format(data[1])
            #seq=data[1]
            
            enddate = datetime.today().strftime('%d-%m-%Y')
           
            now = data[15]
           
            endtime = now.strftime("%H%M%S")
           
            headers= {
            "Accept": "application/json",
            "Content-Type": "application/json"
               }
            
            oxystd = ""
            oxyact = 0.0
            if jsondata['PTN'] == "PTN-5":
                oxystd = data[14]
                oxyact = data[13]
            
            dict1 ={"DB1_PV":data[7],"DB1_SV":data[6],"DB2_PV":"","DB2_SV":"","KP_PV":data[5],"KP_SV":data[4],
                        "OXY_ACT":float("{:.3f}".format(oxyact)),"OXY_STD":oxystd,"SEQ":seq,"STEP_NO":data[3],"TIME":dt_string}
            
        
            jsondata["TEMPERATURE_LIST"].append(dict1)
            jsondata["END_TIME"]=endtime
            jsondata["END_DATE"]=str(enddate)
           
            jsondata1=json.dumps(jsondata)
            print(jsondata1)
            
            headers= {
            "Accept": "application/json",
            "Content-Type": "application/json"
               }
            
            
            r=requests.put(complete_url3,data={"data":jsondata1},headers=headers)
            print(r.content)
            print(r.status_code)
        
            query1 = "INSERT INTO [db_resibon].[dbo].[{0}] (machine,END_DATE,END_TIME) VALUES (?,?,?)".format(machineNo)
            today = date.today()
            
            machineno = machineNo
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
           

            data_employee = (machineno,today,dt_string)
            try:
                pnx = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=THAIPLC\MSSQLRESIBON;"
                              "Database=db_resibon;"
                              "Trusted_Connection=yes;")
                cursor = pnx.cursor()
                cursor.execute(query1, data_employee)
                pnx.commit()
                pnx.close()
            except Exception as e:
                print("Database Exception  - 2")
                print(e)
                
            
            
            
                
    except Exception as e:
        print("Put data end exception")
        print (e)     
    
    print("END URLEND")          

schedule.every(1).seconds.do(start)
print("Starting...")
while 1:
    schedule.run_pending()
    time.sleep(1)
