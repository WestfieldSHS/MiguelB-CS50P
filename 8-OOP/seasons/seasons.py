from datetime import date

def main():
    dob = input("When were you born? YYYY-MM-DD: ")
    dob = date.fromisoformat(dob)
    today = date.today()
    years_lived = today.year - dob.year
    total_leap_years = round(years_lived/4, 1)
    total_minutes = (years_lived-total_leap_years)*525600 + total_leap_years*(525600+1440)
    print(total_minutes)

main()