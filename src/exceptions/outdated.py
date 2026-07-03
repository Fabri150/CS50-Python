months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        else:
            month, day, year = date.split()
            if month not in months:
                raise ValueError
            if not day.endswith(","):
                raise ValueError
            day = day.replace(",", "")
            month = months.index(month) + 1
            day = int(day)
            year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31 and year <= 9999:
            break
    except ValueError:
        pass

print(f"{year:04}-{month:02}-{day:02}")