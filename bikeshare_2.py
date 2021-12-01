import time
import pandas as pd
import numpy as np


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s Explore Some US Bikeshare Data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Enter The City You're Curious About: ").lower()
    city_name=['chicago','new york city','washington']
    while True:
        if city not in city_name:
            city=input("Please Enter A Valid City Name(chicago, new york city, washington): ").lower()
        else:
            break

    # get user input for month (all, january, february, ... , june)
    month=input("Now Enter The Month You Want To Know More About(all/january:june): ").lower()
    month_name=['all', 'january', 'february', 'march', 'april','may', 'june']
    while True:
        if month not in month_name:
            month=input("Please Enter A Valid Month Name(all, january, february, march, april, may, june): ").lower()
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Now Enter The Week Day(all/Monday:Sunday): ").title()
    day_name=['All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while True:
        if day not in day_name:
            day=input("Please Enter A Valid Day Name(all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").title()
        else:
            break

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
    
    CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }
    df= pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    months = {'january':1 , 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
    if month != 'all':
        df = df[df['month']==months[month]]
    
    if day != 'All':
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times Of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    if month =='all':
        months = {1:'January' , 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
        print('The Most Common Month Is:', months[df['month'].mode()[0]])
        
    # display the most common day of week
    if day=='All':
        print('The Most Common Week Day Is:', df['day_of_week'].mode()[0])
    
    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    h=df['hour'].mode()[0]
    if h == 12:
        print('The Most Common Start Hour Is: 12 PM')
    elif h > 12:
        h=h-12
        print('The Most Common Start Hour Is:', h, 'PM')
    else:
        print('The Most Common Start Hour Is:', h, 'AM')
     
    print("\nThis Took %s Seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations And Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The Most Common Start Station Is:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The Most Common End Station Is:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Trip Road']=df['Start Station']+ ' ---> ' +df['End Station']
    print('The Most Frequent Combination Of Start Station And End Station Trip Is:', df['Trip Road'].mode()[0])

    print("\nThis Took %s Seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The Total Travel Time Is:', round(df['Trip Duration'].sum()/3600,3), 'Hours.')
 

    # display mean travel time
    print('The Average Travel Time Is:', round(df['Trip Duration'].mean()/60,2),'Minutes.')

    print("\nThis Took %s Seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
   
    # Display counts of user types
    print('Counts Of User Types:\n', df['User Type'].value_counts())
    
    if city!= 'washington':
      # Display counts of gender
      print('\nCounts Of Gender:\n', df['Gender'].value_counts())

      # Display earliest, most recent, and most common year of birth
      print('\nEarliest Birth Year Is:',int(df['Birth Year'].min()))
      print('Most Recent Birth Year Is:',int(df['Birth Year'].max()))
      print('Most Common Birth Year Is:',int(df['Birth Year'].mode()[0]))



    print("\nThis Took %s Seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    '''
    displaying some rows of the table upon user's request
    '''

    user_choice= input('Do You Want To Explore Your Table?(y/n) ').lower()

    while True:
        if user_choice == 'y' or user_choice == 'n' :
            break
        else:
           user_choice=input("Please Enter A Valid Answer:(y/n) ").lower()

    if user_choice=='n':
        print('-'*40)
        return

    else:
        start=0
        end=5

        print('\nYour Filtered Table Result Is:\n',df.iloc[start:end])
        print('-'*40)

        while True:
            start=start+5
            end=end+5

            #check if the table has more data
            if start > len(df.index)-1:
                print("No More Data To View.")
                print('-'*40)
                break

            user_choice=input('Do You Want To See More?(y/n) ').lower()
            while True:
                if user_choice == 'y' or user_choice == 'n' :
                    break
                else:
                    user_choice=input("Please Enter A Valid Answer:(y/n) ").lower()
                    
            if user_choice=='y':
                print('\nViewing Next 5 Rows:\n',df.iloc[start:end])
                print('-'*40)
            else:
                break
    print('-'*40)


if __name__ == "__main__":
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while True:
            if restart == 'yes' or restart == 'no' :
                break
            else:
                restart=input("Please Enter A Valid Answer:(yes/no) ").lower()
        if restart != 'yes':
            break