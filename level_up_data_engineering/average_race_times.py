import re
import datetime

def main():

    def get_data():
        with open("10k_race_times.txt", "rt") as file: 
            content = file.read() 
        return content # imports data into a variable that python can read and access easily 

    def get_rhines_times():
        races = get_data() 
        matches = []
        for line in races.splitlines(): # splits the races variable into its individual lines so that each athlete is a seperate data set 
            match = re.search(r"Rhines", line) # checks every line for instance of "Rhines" 
            if match:
                clean = re.search(r"\d{2}:\d{2}", line) 
                matches.append(clean.group()) # if the line matches then that line will be added to the matches dictionary
            else:
                next # if not the loop moves on with no actoin 
        return matches

    def get_average():
        sum = datetime.timedelta() 
        average = datetime.timedelta()
        count = 0
        races = get_data()
        times = []
        for line in races.splitlines():
            match = re.search(r"Rhines", line) # the same as the previous function, however now we want a more specific outcome
            if match:
                clean = re.search(r"\d{2}:\d{2}", line) # searches the line for a specific string which has 00:00 formatting, which would have to be the time
                times.append(clean.group()) # takes that string and appends only the match to the times list, to return just the match use the .group() function from re
                count += 1 # count has to be incremented to know how many times  to divide to get the average
            else:
                next       
        for time in times:
            (m,s) = time.split(':')
            d = datetime.timedelta(minutes=int(m), seconds=int(s))
            sum += d # each time is added to sum using datetime function timedelta, this is not super accurate because it uses float 
            average = sum / count
        return average

        

    print(get_rhines_times())


if __name__ == "__main__":
    main()