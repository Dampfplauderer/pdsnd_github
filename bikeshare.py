import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        city = input("Please enter the city (chicago,washington,new york city) you would like to analyze: ").lower()

        if city in ["chicago","washington","new york city"]:

         break

        else :
            print("please enter city again")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        month = input("Please enter the month you want data for: ").lower()

        if month in ["january", "february", "march", "april", "may", "june", "all"]:

            break

        else:

            print("This month doesn't exist. Please choose another one")




    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        day = input("Please enter the day(s) you want data for: ")

        if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:

                break

        else:

            print("This day doesn't exist. Please choose another one")


    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode().max()
    print("the most popular month is",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode().max()
    print("the most popular day is", popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode().max()
    print("the most popular hour is", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].mode().max()
    print("Most common Start Station: ",start_station)

    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode().max()
    print("Most common End Station: ",end_station)
    # TO DO: display most frequent combination of start station and end station trip
    start_end_combi = (df["Start Station"] +" - " + df["End Station"]).mode().max()
    print("Most common combination of Start and End Station: ",start_end_combi)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tt_time = df["Trip Duration"].sum()
    print("The total Travel time is: ",tt_time)

    # TO DO: display mean travel time
    mean_tt = df["Trip Duration"].mean()
    print("The mean Travel time is: ",mean_tt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if "User Type" in df.columns:
        user_type = df["User Type"].value_counts()
    print("Number of customer vs. subscriptions\n",user_type)

    # TO DO: Display counts of gender
    try:
        gender_count = df["Gender"].value_counts()
        print("Male vs. Female renters\n",gender_count)
    except:
        print("No Gender information available for this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthday = df["Birth Year"].min()
        print("The earliest year of birth is: ",earliest_birthday)
        recent_birthday = df["Birth Year"].max()
        print("The most recent year of birth is: ",recent_birthday)
        common_birthday = df['Birth Year'].mode()
        print("The most common year of birth is: ",common_birthday)
    except:
        print('There is no birth year information for this city.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Ask's the user if he would like to see 5 lines of the raw data and adds more until the user inputs 'no'"""
    lines_d = 0

    while True:

        question = input("Do you want to get a glimpse at few lines of the raw data first? Enter yes or no\n").lower()
        if question == "yes":
            lines_d += 5
            print(df.iloc[0 :lines_d])
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
