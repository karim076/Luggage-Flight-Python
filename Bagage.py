import csv
from logging import getLogRecordFactory
import os
from datetime import datetime
from datetime import timedelta
#clear screen
os.system("cls")
# import CSV into dictionary-List
bagageFile = open("bagage.csv", "r")
reader = csv.DictReader(bagageFile)
bagageList= list(reader)
#Variables
# vraag1
totalWeight = 0
count = 0
averageWeight = 0
#Vraag2
weightFlight = 0
#vraag3
counter = 0
#vraag 4
averageWeightArrival = 0
#Dit def functie wordt gebruikt om telkens terug te gaan of om te stoppen
def returnBack():
    print("--------------------------")
    print("Als u wilt stoppen type X als u terug wilt klik enter")
    returnAnswer = input("Uw keuze >: ")
    if returnAnswer == "x" or returnAnswer == "X":
        exit()
    else:
        os.system("cls")
        pass
#We hebben count vaker nodig dus maken we een method
for bagage in bagageList:
    count += 1


isRunning = True
while (isRunning):
    #het Menu
    print("Toon mij...")
    print("1. Gemiddelde gewicht van alle vervoerde bagage")
    print("2. Totale gewicht voor vlucht met nummer X")
    print("3. Gemiddelde gewicht van alle stukken vervoerd door maatschappij X met bestemming Y")
    print("4. Aantal stukken voor bestemming X met een incident")
    print("5. Aantal stukken van maatschappij X met een incident, die zijn ingeladen door medewerker Y")
    print("6. Aantal dieren waarbij een incident plaatsvond, geteld voor maatschappij X")
    print("7. Aantal dieren waarbij een incident plaatsvond, geteld voor medewerker X")
    print("8. Gemiddeld aantal overstappen voor breekbare stukken, vervoerd door maatschappij X")
    print("9. Aantal breekbare stukken met een incident dat door maatschappij X is vervoerd in ruim Y")
    print("10. Aantal incidenten in de 30 dagen vanaf datum X")
    print("11. Top 20 bagagestukken met het hoogste gewicht\n")
    #keuze maken
    answer = input("Uw keuze: ")
    os.system("cls")
    #Process
    if answer == "1":
        for bagage in bagageList:
            totalWeight += float(bagage["totaal_gewicht"])
        averageWeight = totalWeight / count
        print(averageWeight)
        returnBack()
    elif answer == "2":
        question = input("Voer een vluchtnummer in: ")
        for bagage in bagageList:
            if bagage["vlucht"] == question:
                weightFlight += float(bagage["totaal_gewicht"])
            print(f"Totale gewicht van vlucht{question} is {weightFlight}")
            returnBack()
    elif answer == "3":
        weightDestination = 0
        company = input("Voer een maatschapij in: ")
        destination = input("Vooer het bestemming in: ")
        for bagage in bagageList:
            if bagage["maatschappij"] == company:
                if bagage["bestemming"] == destination:
                    weightDestination += float(bagage["totaal_gewicht"])
                    counter += 1
        averageWeightArrival = weightDestination / counter
        print(f"gemiddelde gewicht voor{company} met bestemming{destination} is {averageWeightArrival}kg")
        returnBack()
    elif answer == "4":
        counterFour = 0
        destination = input("Voer een bestemming in: ")
        for bagage in bagageList:
            if bagage["bestemming"] == destination:
                if bagage["incidenten"] != "":
                    counterFour += 1
        print(f"aantal incidenten in richting {destination} is {counterFour}")
        returnBack()
    elif answer == "5":
        counterFive = 0
        company = input("Voer een maatschapij in: ")
        worker = input("Voer medewerker in: ")
        for bagage in bagageList:
            if bagage["maatschappij"] == company:
                if bagage["ingeladen_door"] == worker:
                    if bagage["incidenten"] != "":
                        counterFive += 1
        print(f"aantal incidenten in richting {company} met {worker} is {counterFive}")
        returnBack()
    elif answer == "6":
        counterSix = 0
        company = input("Voer een maatschapij in: ")
        for bagage in bagageList:
            if bagage["maatschappij"] == company:
                if bagage["dieren"] == "1":
                    if bagage["incidenten"] != "":
                        counterSix += 1
        print(f"aantal incidenten met een dier voor maatschappij {company} is {counterSix}")
        returnBack()
    elif answer == "7":
        counterSeven = 0
        worker = input("Voer medewerker in: ")
        for bagage in bagageList:
            if bagage["ingeladen_door"] == worker:
                if bagage["dieren"] == "1":
                    if bagage["incidenten"] != "":
                        counterSeven += 1
        print(f"aantal incidenten met een dier voor medewerker {worker} is {counterSeven}")
        returnBack()
    elif answer == "8":
        totalItems = 0
        totalBreakable = 0
        company = input("Voer een maatschapij in: ")
        for bagage in bagageList:
            if bagage["maatschappij"] == company:
                if bagage["breekbaar"] == "1":
                    totalItems += float(bagage["aantal_stuks"])
                    totalBreakable += float(bagage["breekbaar"])
        averageTotal = totalItems / totalBreakable    
        print(f"Gemiddelde overstappen vor breekbare items bij {company}: {averageTotal}")
    elif answer == "9":
        company = input("Voer een maatschapij in: ")
        room = input("Voer een ruimte in: ")
        counter = 0
        for bagage in bagageList:
            if bagage["maatschappij"] == company:
                if bagage["vrachtruim"] == room:
                    if bagage["breekbaar"] == "1":
                        if bagage["incidenten"] != "":
                            counter += 1
        print(f"Aantal breekbare stukken met een incident dat door maatschappij {company} en in {room} is: {counter}")
        returnBack()
    elif answer == "10":
        start_Date =  input("Voer een datum in (YYYY/mm/dd): ")
        start_date = datetime.strptime(start_Date,"%Y/%m/%d")
        end_Date = start_date + timedelta(days=30)
        counter = 0
        for bagage in bagageList:
            bagage['vertrekdatum'] = datetime.strptime(bagage["vertrekdatum"], "%Y/%m/%d")
            if bagage["vertrekdatum"] > start_date and bagage["vertrekdatum"] < end_Date:
                if bagage["incidenten"] != "":
                    counter += 1
        print(f"Aantal incidenten in de 30 dagen vanaf {start_date} tot {end_Date} is {counter}")
        returnBack()
    elif answer == "11":
        counter = 0
        data_sorted=sorted(bagageList ,key=lambda row:float(row["totaal_gewicht"]),reverse=True)
        for i in range(20):
            top20 = data_sorted[i]
            counter += 1
            print(f"{counter}. {top20['totaal_gewicht']} op vlucht {top20['vlucht']} naar {top20['bestemming']}")
        returnBack()

