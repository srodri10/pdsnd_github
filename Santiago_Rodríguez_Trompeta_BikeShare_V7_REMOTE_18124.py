# -*- coding: utf-8 -*-
"""Bikeshare
by Santiago Rodríguez Trompeta
Date of Creation: 19th November 2022
"""

import time
import pandas as pd
import numpy as np

#Creating a dictionary containing the data sources for the three cities

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'total': 7}

DAYS_LIST = ['total', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

OPTIONS = ['yes', 'no']


def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """

    rdata = ''

    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in OPTIONS:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes \nNo \n(not case sensitive)")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in OPTIONS:
            print("\nInvalid input. Please enter a valid input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")


#Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
            print(df[counter:counter+5])
        elif rdata != "yes":
             break

print('-'*70)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print(' ')
    print('Hello! My name is Santiago and we are going to explore some US bikeshare data!')
    print(' ')
    time.sleep(2)
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Which city you would like to analyze?\n 1 Chicago\n 2 New York City\n 3 Washington'\
                     '\nAccepted input:\nFull name of city; not case sensitive (e.g. chicago or CHICAGO).').lower()

    while city not in CITY_DATA:
            print('Please check your input, it doesn\'t appear to be conforming to any of the accepted input formats or spelling')
            city = input('Which city you would like to analyze? chicago, new york city or washington?')

    print(f"\nYou have chosen {city.title()} as your city.")



    # get user input for month (all, january, february, ... , june)
    month = input('Which month you would like to analyse from january to june?'\
    'Or simply all of them?, In the last case type \'total\'').lower()
    while month not in MONTH_DATA:
        print('Seems like there is a typo or something else, please consider your spelling!')
        month = input('Which month you would like to analyse from january to june? Or simply all of them?').lower()

    print(f"\nYou have chosen {month.title()} as your period of time.")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day you would like to analyse?\n (Monday, Tuesday, Wednesday...)\n Or simply all of them?'\
    'In the case type \'total\'').lower()
    while day not in DAYS_LIST:
        print('Please check your input, consider your spelling!')
        day = input('Which day you would like to analyse? Or simply all of them?').lower()

    print(f"\nYou have chosen {day.title()} as your day of the week.")



    return city, month, day

    print('-'*70)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #Load data for city
    print("\nLoading data...")
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #Filter by month if applicable
    if month != 'total':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'total':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df



def time_stats(df, city):
    """statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month_num = df['Start Time'].dt.month.mode()[0]


    print('1) The most popular month in', city, 'is:', popular_month_num,'(1 = January,...,6 = June)')



    # display the most common day of week


    popular_day_of_week = df['day_of_week'].mode()[0]

    print('2) The most popular weekday in', city, 'is:',popular_day_of_week)





    # display the most common start hour


    popular_start_hour = df['hour'].mode()[0]

    print('3) The most popular starting hour in', city, 'is:',popular_start_hour)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*90)




def station_stats(df, city):
    """statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    popular_start_station_amount = df['Start Station'].value_counts()[0]
    print('1) The most popular start station in', city, 'is:',popular_start_station, 'and was used', popular_start_station_amount, 'times.')



    # display most commonly used end station

    popular_end_station = df['End Station'].mode()[0]
    popular_end_station_amount = df['End Station'].value_counts()[0]
    print('2) The most popular end station in', city, 'is:',popular_end_station, 'and was used', popular_end_station_amount, 'times.')



    # display most frequent combination of start station and end station trip


    popular_trip = df.groupby(["Start Station", "End Station"]).size().idxmax()
    popular_trip_amt = df.groupby(["Start Station", "End Station"]).size().max()
    print('3) The most popular trip is:\n', popular_trip, '\n and was driven', popular_trip_amt,'times')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*90)


def trip_duration_stats(df, city):
    """statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()



    # display total travel time

    df['Time Delta'] = df['End Time'] - df['Start Time']
    total_time_delta = df['Time Delta'].sum()
    print('1) The total travel time was:', total_time_delta)



    # display mean travel time

    total_mean = df['Time Delta'].mean()
    print('2) The mean travel time was about:', total_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*90)



def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print('1) The total users by type in', city, 'are as followed:\n', df['User Type'].value_counts())
    print('*'*70)





    # Display counts of gender
    try:
        genders = df['Gender'].value_counts()
        print("Gender:")
        print(genders)
        print()
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!")


     # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('3) The age structure of our customers in', city, 'is:\n' 'Oldest customer was born in:', int(earliest_year),'\n' 'Youngest customer: was born in:', int(most_recent_year),'\n' 'Most of our customer are born in:', int(most_common_year))
    except Exception as e:
        print("There isn't a [Birth Year] column in this spreedsheet!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)
    print('-'*32,"END",'-'*33)
    print('-'*70)







def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
