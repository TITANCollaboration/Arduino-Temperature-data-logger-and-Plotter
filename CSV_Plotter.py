import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import os 

def csv_input():# The function for the intake csv files , asks for user input on the files, checks if they are valid and asks how you would like the plot to be made
    while True:
        raw_input = input("Enter desired CSV file paths in a comma seperated list.\n>").strip()
        stacked = input("Would you like the plots for the files seperate or all on one plot? Please answer stacked or seperate")
        
        if not raw_input:
            print("No input provided.\n")
            continue
        raw_path = raw_input.split(",")

        valid = []
        invalid = []

        for path in raw_path:
            clean_path = path.strip().strip("'\"")
            if clean_path:
                if os.path.isfile(clean_path) and clean_path.lower().endswith(".csv"):
                    valid.append(clean_path)
                else:
                    invalid.append(clean_path)
        if invalid:
            print("Could not find the following files")
            for bad in invalid:
                print("f -{bad}")
        if valid:
            return valid, stacked


def Temp_plots(file_list, plot): #The plotting function which can either plot on seperate plots that save to the computer or save multiple days worth of data onto one graph

    if plot == "stacked":# This is for multiple days on one graph, takes the data and forms one graph that each days graphs get layed on and "stacked"
        fig, ax = plt.subplots()
        for file in file_list:
            print("Reading: {file}")
            temp = []
            time = []
            


            try:
                with open(file, mode="r", encoding = "utf-8") as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:

                        if not row:
                            continue
                        timestr = row[0]

                        try:
                            temp_val = float(row[1])
                            temp.append(temp_val)
                            time.append(timestr)
                        except(ValueError, IndexError):
                            continue        
            except Exception as e:
                print(f"Error reading file")
            
            
            ax.plot(time,temp,label=f"{file}")
                
        ax.set_title("PB5 Temperature over time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Temperature in degrees celcius")
        ax.legend()
        plt.show()            

            
        


    else:# This is for saving them as png files and saving as individual day graphs 
                    
        for file in file_list:
            print("Reading: {file}")
            temp = []
            time=[]
            try:
                with open(file, mode="r", encoding="utf-8") as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:

                        if not row:
                            continue

                        timestr=row[0]

                        try:
                            temp_val = float(row[1])

                            temp.append(temp_val)
                            time.append(timestr)
                        except (ValueError, IndexError):

                            continue
                times = [datetime.strptime(t, "%H:%M:%S")for t in time]

                plt.figure()
                plt.plot(times, temp)
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
                plt.xticks(rotation=45)
                plt.title(f"Change in PB5 Power supply temperature ")
                plt.xlabel("Time in Hour : Minute : Second")
                plt.ylabel("Temperature in degrees celcius ")
                plt.savefig(f"{file}.png")
                plt.close()
            except Exception as e:
                print(f" Error reading file: {e}\n")

def main(): # Main fuction that calls on the others 
    print("CSV plotter")
    files, plot = csv_input()
    Temp_plots(files, plot)

if __name__ == "__main__":
    main()





                
