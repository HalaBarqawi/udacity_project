Here's your `README.md` formatted as requested:

```
# BikeShare Data Analysis

## Overview
This program allows users to explore bikeshare data for **Chicago**, **New York City**, and **Washington**. Users can filter data by city, month, and day of the week, and view statistics on trip durations, popular stations, user data, and more. It also allows viewing raw data in increments of 5 rows.

## Functions

- **`get_filters()`**: Prompts the user to select a city, month, and day of the week to filter the data.
- **`load_data(city, month, day)`**: Loads the bikeshare data for the specified city and filters it based on the chosen month and day.
- **`display_raw_data(df)`**: Displays raw data in increments of 5 rows, allowing the user to see more data on request.
- **`time_stats(df)`**: Displays statistics on the most frequent times of travel (month, day of the week, start hour).
- **`station_stats(df)`**: Displays statistics on the most popular stations and trips.
- **`trip_duration_stats(df)`**: Displays statistics on the total and average trip duration.
- **`user_stats(df)`**: Displays statistics on bikeshare users, including user types, gender, and birth year.
- **`main()`**: Main function that runs the program, calls other functions, and allows the user to restart or exit.

## Example Output

```plaintext
Hello! Let's explore some US bikeshare data!
Which city would you like to explore? (chicago, new york city, washington): chicago
Which month would you like to explore? (all, january, february, ... , june): january
Which day of the week would you like to explore? (all, monday, tuesday, ... sunday): all
----------------------------------------
Would you like to see 5 lines of raw data? Enter yes or no: yes
   Start Time            End Time  Trip Duration   Start Station    End Station  User Type
0  2017-01-01 00:06:00  2017-01-01 00:16:00  600          Station A     Station B    Subscriber
1  2017-01-01 00:12:00  2017-01-01 00:22:00  600          Station B     Station C    Customer
...
Most common month: 1
Most common day of the week: Monday
Most common start hour: 6
...
```

## Dependencies
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical operations (if required).
- **time**: Time calculations for performance.

## How to Run
Place the CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory as the script.

Run the program:
```bash
python bikeshare_2.py
```
```
