
import pandas as pd
import numpy as np
import time


CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_data():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('='*70)
    print('\nHello! Let\'s explore some US bikeshare data!')
    print()

    # Get user input for city (chicago, new york city, washington), Using a while loop to handle invalid inputs
    city = input('Enter the name of the city to analyze data. (E.g. Enter either Chicago, New York, Washington): ').lower()
    while city not in ['chicago', 'new york', 'washington']:
        print("\nInvalid data or incorrect spelling, Please enter either chicago, new york city or washington.\n")
        city = input('Enter the name of the city to analyze data. (E.g. Enter either Chicago, New York, Washington): ').lower()

    # Get user input for month (all, january, february, ... , june)
    print()
    months = ["january", "february", "march","april", "may", "june", "all"]
    month = input("Enter the name of the month to filter data. (E.g January, February, March, April, May, June or all): ").lower()
    while month not in months:
        print("\nInvalid data or incorrect spelling, Please enter either 'all' or any month from january to june.\n")
        month = input("Enter the name of the month to filter data. (E.g January, February, March, April, May, June or all): ").lower()

    # Get user input for day of week (all, monday, tuesday, wednesday, thursday, friday, sunday) 
    print()  
    days = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input("Enter the name of the day to filter data. (E.g. Enter either Monday, Tuesday, Wednesday, Thursday, Friday. Saturday, Sunday or all): ").lower()
    while day not in days:
        print('\nInvalid data or incorrect spelling, Please enter either day name from monday to sunday.\n')
        day = input("Enter the name of the day to filter data. (E.g. Enter either Monday, Tuesday, Wednesday, Thursday, Friday. Saturday, Sunday or all): ").lower()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #this extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    # this extract a day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if the user specify the month name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if the user specify the day name
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def popular_time_statistics(df):
    """Displays statistics on the most popular times of travel."""
    print('='*70)
    print('\nCalculating The Most Popular Times of Travel..........\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print("\nThe most popular month is: ", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print("\nThe most popular day is: ", popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("\nThe most popular hour is: ", popular_hour)
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)


def popular_station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip..........\n')
    start_time = time.time()

    # display most common start station
    common_start_station = df["Start Station"].value_counts().idxmax()
    print("\nThe most common start station is: ", common_start_station)

    # display most common end station
    common_end_station = df["End Station"].value_counts().idxmax()
    print("\nThe most common end station is: ", common_end_station)
   

    # display most frequent combination of start station and end station trip
    df['frequent combination'] = df['Start Station'] + "-" + df['End Station']
    frequent_combination = df['frequent combination'].value_counts().idxmax()
    print("\nThe most common trip from start to end is: ", frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)


def trip_duration_statistics(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration..........\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("\nTotal travel time is: {} hours".format(total_travel_time / 3600.0))

    # display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("\nAverage travel time is: {}  hours".format(average_travel_time / 3600.0))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)


def user_info_statistics(df):
    """Displays statistics on users."""

    print('\nCalculating User Info Statistics..........\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of each User Type")
    counts_of_userType = df["User Type"].value_counts()
    print(counts_of_userType)
    
    # Display counts of gender
    print()
    try:
        print("Counts of each Gender")
        counts_of_gender = df["Gender"].value_counts()
        print(counts_of_gender)
    except:
        print("\nNo data available about gender for Washington\n")

    # Display earliest, most recent, and most common year of birth
    print()
    try:
        earlies_year_of_birth = int(df["Birth Year"].min())
        print("\nThe earliest year of birth is:", earlies_year_of_birth)

        most_recent_year_of_birth = int(df["Birth Year"].max())
        print("\nThe most recent year of birth  is:", most_recent_year_of_birth)

        most_common_year_of_birth = int(df["Birth Year"].value_counts().idxmax())
        print("\nThe most common year of birth is:", most_common_year_of_birth)
    except:
        print("No data available about birth year for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*70)

#   Function displays five rows of data of the choosen city.
def display_raw_data(city):
    
    df = pd.read_csv(CITY_DATA[city])
    next = 0
    while True:
        raw_data = input("Would you like to display next five row of raw data? Please Enter Yes or No: ").lower()
        if raw_data not in ["yes", "no"]:
            print("\nInvalid Answer! Please type Yes or No.\n")
        elif raw_data == "yes":
            print()
            print(df.iloc[next:next + 5])
            next += 5
            print()
        elif raw_data == "no":
            break


def main_menu():
    while True:
        city, month, day = get_data()
        df = load_data(city, month, day)

        popular_time_statistics(df)
        popular_station_statistics(df)
        trip_duration_statistics(df)
        user_info_statistics(df)
        display_raw_data(city)
        
        print()
        restart = input('Would you like to restart? Enter Yes or No: ')
        if restart.lower() != 'yes':
            break
    
    print("\nThank you for using this program! Goodbye!\n")

if __name__ == "__main__":
    main_menu()