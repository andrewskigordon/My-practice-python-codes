#my subway infomatiion code
string1 = input("nyc subway rolling stock information\npess enter to contune: ")
print(string1)

#Nyc subway class section

class nyc_subway_train:

    def __init__(self,type,manufacture,year_introduced,cbtc):
        self.type = type
        self.manufacture = manufacture
        self.year_introduced = year_introduced
        self.cbtc = cbtc

R211 = nyc_subway_train("R211","kawasaki","2023","yes")
R179 = nyc_subway_train("R179","Alstom","2017","yes")
R46 = nyc_subway_train("R46","pullman","1976","no")
R68 = nyc_subway_train("R68","Westinghouse amrail","1986","no")
R32 = nyc_subway_train("R32","Budd company","1968","no")
R44 = nyc_subway_train("R44","St luis car company","1972","no")

#Get train information by puting the class type and self info into the line 25
#note that all inputs are default and on the first line

print(R211.year_introduced)
print("this is evaluating the data of subway cars and there cababilities with the new subway control systems\nyou can also find important information like manufacture\nthe year of the ontroduction of the train\nand if its combatible with CBTC ""\"communication based train control\" or not")
string2 = input("pess enter to continue: ")
print(string2)

#NYC subway railcar facts section 

subway_car_age_facts = {
    2017:"R179 intruced in 2017 to replace the aging r42 and r32 railcars",
    1976:"introduced in 1976, it was the last pullman standerd manufactured railcar to made by pullman standard",
    1986:"R68 was the third and last railcar to be 75 feet long",
    2023:"R211 is the newest subway car in the system, it is also the first subway railcar to feture open gangway technolegy",
    1968:"Know as the ""\"Brightliners\" they were the longest serving subway cars in the world from 1968 to 2021",
    1972:"The R44 was the last railcar to be built the st luis car company and the first 75ft railcar on the NYCTA, it is also used on the staten island railway and the subway car to hold the world speed record of the subway car in the world"
    
}

#railcar facts get information sectuon

print(subway_car_age_facts.get(2023))
string4 = input("now lets go accross the atlantic ocean\npress enter to continue: ")
print(string4)

#london underground facts section
#london underground class

class london_underground():

    def __init__(self,stock_type,line,ATO,over_45_years_of_age):
        self.stock_type = stock_type
        self.line = line
        self.ATO = ATO
        self.over_45_years_of_age = over_45_years_of_age

TFL0 = london_underground("1992 stock","central line","yes","no")
TFL1 = london_underground("1967 stock","Victoria line","yes","no")
TFL2 = london_underground("1972 stock","bakerloo line","no","yes")
TFL3 = london_underground("2009 stock","Victoria line","yes","no")

#note that all inputs are default and on the first line
#Get train information by puting the class type and self info into the line 56

print(TFL0.ATO)
print("this is the rail information for the london underground.")

#london underground dictionaries

TFL_subway_facts = {
    1992:"Central line stock is my personal favorete stock on the london underground\nit was made by British Rail Engineering Limited and Asea Brown Boveri. It used on the longest tube line in london the central line and the waterloo and city line",
    1967:"Victoria line stock, made by metro-Cammell and used on the victoria line from 1967 to 2009, They were the first trains to incoperate Automatic train operation ATO ",
    1972:"bakerloo line stock made by metro-Cammell, very simular to the piccadilly lines 1973 stock due to the order being rushed, they are the oldest EMUs in service in the UK",
    2009:"Victoria line stock, replacing the 1967 stock. The new stock enables TFL to use communications based train control, witch allows trains to run every 90 seconds",
}

#note that all inputs are default and on the first line

print(TFL_subway_facts.get(1992))
streng = input("thank you for run this code\nTo view deferent values, please change the values and rerun the code. ")
print(streng)


