import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks for input to filter the dataset by city, month, and day of the week.
    It ensures that the user's input is valid and within the available options.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    city = input("Which city would you like to explore? (chicago, new york city, washington): ").lower()
    while city not in CITY_DATA:
        print("Sorry, invalid input. Please choose from chicago, new york city, or washington.")
        city = input("Which city would you like to explore? (chicago, new york city, washington): ").lower()

    # Get user input for month
    month = input("Which month would you like to explore? (all, january, february, ... , june): ").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months:
        print("Sorry, invalid month input. Please choose a month from january to june or 'all'.")
        month = input("Which month would you like to explore? (all, january, february, ... , june): ").lower()

    # Get user input for day
    day = input("Which day of the week would you like to explore? (all, monday, tuesday, ... sunday): ").lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
        print("Sorry, invalid day input. Please choose a day from monday to sunday or 'all'.")
        day = input("Which day of the week would you like to explore? (all, monday, tuesday, ... sunday): ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads the bikeshare data for the specified city and filters it by month and day if applicable.

    The function reads the data for the selected city and converts the 'Start Time' column to datetime.
    It then filters the data based on the selected month and day of the week.

    Args:
        city (str): The city for which to load data (chicago, new york city, washington).
        month (str): The month to filter by, or "all" for no filtering.
        day (str): The day of the week to filter by, or "all" for no filtering.

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data for the selected city
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month != 'all':
        # Filter by month
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Start Time'].dt.month == month_index]

    # Filter by day if applicable
    if day != 'all':
        # Filter by day of week
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df


def display_raw_data(df):
    """
     The function will ask the user if they want to view more data. The user can continue to see raw data 
    in chunks of 5 rows, and the program will stop when there is no more data left to display.

    Args:
        df (pandas.DataFrame): The DataFrame containing the bikeshare data.
    """
    start_row = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if show_data == 'yes':
            print(df.iloc[start_row:start_row+5])
            start_row += 5
            if start_row >= len(df):
                print("No more data to display.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def time_stats(df):
    """
     Displays statistics on the most frequent times of travel.

    The function calculates and prints the most common month, day of the week, and hour of the day for 
    trips in the dataset.

    Args:
        df (pandas.DataFrame): The DataFrame containing the bikeshare data.    
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month
    popular_month = df['Start Time'].dt.month.mode()[0]
    print(f"Most common month: {popular_month}")

    # Most common day of the week
    popular_day_of_week = df['Start Time'].dt.day_name().mode()[0]
    print(f"Most common day of the week: {popular_day_of_week}")

    # Most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trips.

    The function calculates and prints the most common start station, end station, and the most frequent 
    combination of start and end stations (i.e., the most popular trip).

    Args:
        df (pandas.DataFrame): The DataFrame containing the bikeshare data.
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most common start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most common start station: {popular_start_station}")

    # Most common end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most common end station: {popular_end_station}")

    # Most frequent combination of start and end stations
    popular_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"Most common trip: {popular_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    The function calculates and prints the total travel time and the mean travel time for trips in the 
    dataset.

    Args:
        df (pandas.DataFrame): The DataFrame containing the bikeshare data
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    The function calculates and prints the counts of user types, gender, and birth year (if available) 
    from the dataset.

    Args:
        df (pandas.DataFrame): The DataFrame containing the bikeshare data.
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(f"User Type Counts:\n{user_type_counts}")

    # Counts of gender (if available)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(f"Gender Counts:\n{gender_counts}")

    # Earliest, most recent, and most common birth year (if available)
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Display raw data if the user wants to
        display_raw_data(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
