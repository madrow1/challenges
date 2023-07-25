import re # imports python regex library 
from datetime import datetime, time # imports datetime and time from the python datetime library

def calc_age(dob, race): # sets up a function to calculate the age of an athlete based on their date of birth and the date of the race in question
    age_at_race_delta = [] 
    format = '%d %b %Y' # uses date time to format strings into date objects for calculation purposes
    age = datetime.strptime(dob, format) # uses the .strptime function to convert string to date object
    age_at_race = []

    for time in race: # race is passed from the function get_event_time and is a list of dates extracted from 10k_race_times.txt using regex 
        date_of_race = datetime.strptime(time, format)
        age_at_race_delta.append(date_of_race - age)
    
    for delta in age_at_race_delta: # calculates the amount of time in seconds between the dob passed and the race time in the list age_at_race_delta
        years = delta.total_seconds() / (365.2425 * 24 * 3600)
        age_at_race.append((round(years))) # the result of the above is then divided and rounded to the nearest read and appended to age_at_race which is returned to the main function

    return age_at_race

def get_times(content): # sets up a function to extract the times set by a runner in different races, the content that is passed is already cleaned of the times of other athletes 
    times_to_return = []
    for times in content.splitlines():
        time = re.search(r"\d{2}:\d{2}", times) # this regex searches for \d (numbers) {2} that are two characters long : (seperated by a colon)
        if time: 
            times_to_return.append(time.group()) # this is then appended to times_to_return and sent back to the main function
        else:
            next
       
    return times_to_return


def import_data(): # simple function to import date once, that can then be called in different functions, rather than having to read the data in in every function 
    with open("10k_race_times.txt", "rt") as data:
        content = data.read()
    return content  

def get_event_time():
    content = import_data() 
    dob = "01 Jul 1974" # lazily set the date of birth of the athlete we're searching for as a static string 
    dates = []
    clean_age = []

    for line in content.splitlines():
        race = re.search(r"\d{2}\s\w{3}\s\d{4}", line) # sets up a regex that searches for \d (numbers) {2} 2 characters long, \s (space) \w (letters) {3} 3 characters long \s (space) \d (numbers) {4} 4 characters long 

        if race: #if else statement which requires that race is True, else it skips to prevent null results
            dates.append(race.group()) # appends to dates list with .group() which returns only the match from the regex object
        else:
            next

        age_at_race = calc_age(dob, dates) # sets the value of age_at_race to the result of the function calc_age()

        for age in age_at_race:
            clean_age.append("Age: " + str(age)) # Cleans and appends age_at_race to include "Age: " for better legibitlity 
         
        time = get_times(content) # sets the value of time to get_times(content)

    return list(zip(clean_age,time)) #returns a zipped list of tuples including the age of the runner at the time of race and their time running it



def get_age_slowest_times():
    times = get_event_time() #imports the result of get_event_time()
    count = 0
    time_count = 0
    slowest_five_times = []
    slowest_five = []
    slow_times = []

    for results in times:
        slowest_five_dates = datetime.strptime(results[1], "%M:%S")

        slowest_five_times.append(slowest_five_dates.strftime("%M:%S"))
    
    for t in sorted(slowest_five_times, reverse=True): 
        while count <=4:
            slow_times.append(t)
            count += 1 
    
    for i in times:
        if i[1] in slow_times:
            while time_count <=4:
                slowest_five.append(i)
                time_count +=1 

    return slowest_five

print(get_age_slowest_times())