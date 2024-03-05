import pandas as pd


def calculate_demographic_data(print_data=True):
    
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_df = df[df['sex'] == 'Male']
    average_age_men = round(male_df['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = round((bachelors_count / total_count) * 100,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    without_higher_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    high_income_count_with_higher_education = higher_education[higher_education['salary'] == '>50K'].shape[0]
    higher_education_count = higher_education.shape[0]

    high_income_count_without_higher_education = without_higher_education[without_higher_education['salary']== '>50K'].shape[0]
    without_higher_education_count = df.shape[0] - higher_education_count


    higher_education_rich = round((high_income_count_with_higher_education/higher_education_count)*100,1)
    lower_education_rich = round((high_income_count_without_higher_education/without_higher_education_count)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    min_hours_high_income_count = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0]
    total_min_hours_workers_count = num_min_workers.shape[0]

    rich_percentage = round((min_hours_high_income_count / total_min_hours_workers_count) * 100)


    # What country has the highest percentage of people that earn >50K?
    country_groups = df.groupby('native-country')
    country_high_income_percentages = (country_groups['salary'].apply(lambda x: (x == '>50K').mean()) * 100).sort_values(ascending=False)

    highest_earning_country = country_high_income_percentages.idxmax()
    highest_earning_country_percentage = round(country_high_income_percentages.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_income_indians = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = high_income_indians['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


