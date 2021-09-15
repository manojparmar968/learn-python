year = int(input("enter a year: "))

not_leap_year_list = ['sunday','monday','tuesday','wednesday','thrusday','friday','saturday']
leap_year_list = [('sunday','monday'),('monday','tuesday'),('tuesday','wednesday'),('wednesday','thrusday'),('thrusday','friday'),('friday','saturday'),('saturday','sunday')]
count_sunday = 0
for i in leap_year_list:
    if "sunday" in i:
        count_sunday +=1

count_sunday1 = 0
for i in not_leap_year_list:
    if "sunday" in i:
        count_sunday1 +=1

probability_of_53_sundays_in_a_leap_year = count_sunday/len(leap_year_list)
probability_of_53_sundays_in_a_non_leap_year = count_sunday1/len(not_leap_year_list)


if year%4 == 0:
    print("probability of 53 sundays : ", probability_of_53_sundays_in_a_leap_year)    
else:
    print("probability of 53 sundays : ", probability_of_53_sundays_in_a_non_leap_year)

