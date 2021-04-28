# У нас есть кафе. Нам нужно написать программу для работы баристы.
# Перед тем как писать программу, надо создать тестовые данные.

# 1. Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.
# 2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.
# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.
import random, time, datetime

number_of_customers = random.randint(5, 20)
number_of_cups = random.randint(1, 3)


def get_random_date(year, month, day_from, day_to):
    # Set min date
    min_date = datetime.date(year, month, day_from)
    # Set max date
    max_date = datetime.date(year, month, day_to)
    # Get min max timestamps
    min_dt_ts = int(time.mktime(min_date.timetuple()))
    max_dt_ts = int(time.mktime(max_date.timetuple()))

    # Get random timestamp
    random_ts = random.randint(min_dt_ts, max_dt_ts)
    # Get random date
    random_date = datetime.date.fromtimestamp(random_ts)
    return random_date


def get_random_business_date(year, month, day_from, day_to):
    random_date = get_random_date(year, month, day_from, day_to)
    while random_date.isoweekday() in (6, 7):
        random_date = get_random_date()
    return random_date


def get_random_time():
    hours = random.randint(9, 19)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    random_time = '%02d:%02d:%02d' % (hours, minutes, seconds)
    return random_time


def generate_purchase(year, month, day_from, day_to):
    purchase = {}
    i = 1
    while i <= number_of_customers:
        purchase_date_time = [get_random_business_date(year, month, day_from, day_to).strftime('%Y-%m-%d'),
                              get_random_time()]
        purchase[tuple(purchase_date_time)] = random.randint(1, 3)
        i += 1
    return purchase


# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.
def generate_report(year, month, day_from, day_to):
    sum_number_of_cups = 0
    number_of_clients = 0

    # Check whether the current day is last day of week
    if datetime.datetime.now().isoweekday() == 3:
        purchase = generate_purchase(year, month, day_from, day_to)
        for date, day in purchase:
            key = [date, day]
            number_of_cups_per_purchase = purchase[tuple(key)]

            # Calculate total number of cups and clients
            sum_number_of_cups += number_of_cups_per_purchase
            number_of_clients += 1

            # Print details for each purchase
            output = f"Date of purchase is {date}. Time is {day}. Number of cups is {number_of_cups_per_purchase}."
            print(output)

    # Print total
    total = f"Total number of cups {sum_number_of_cups}. Total number of clients {number_of_clients}. "

    return total


print("Task3: generate report")
print(generate_report(2021, 4, 28, 30))


# 4. Нужно посмотреть, в какое время дня у баристы были перерывы в работе.
# Для этого, нужно взять все покупки за каждый день, сравнить время между ними и отобразить промежутки больше часа.
def get_long_breaks(year, month, day_from, day_to):
    # Get purchases
    purchase = generate_purchase(year, month, day_from, day_to)

    # Get unique days when purchases happen
    purchase_day = set()
    for day, t in purchase:
        purchase_day.add(day)
    print(purchase_day)

    # For each day get its time slots, sort them and find deltas
    for day in purchase_day:
        purchase_time = []
        for d, t in purchase:
            if d == day:
                purchase_time.append(t)
        print(f"Day: {day}")

        # Add start and end working hours to each day
        purchase_time.append('09:00:00')
        purchase_time.append('20:00:00')

        # Sort timeslots for each day
        times_sorted = sorted(purchase_time)
        print(f"Time slots are :{times_sorted}")

        # find  deltas and print time slots if delta more than 1 hour
        for i in range(len(times_sorted) - 1):
            delta_in_seconds = (
                    datetime.datetime.strptime(times_sorted[i + 1], "%H:%M:%S") - datetime.datetime.strptime(
                times_sorted[i], "%H:%M:%S")).seconds
            delta_in_hours = delta_in_seconds / 3600
            if delta_in_hours > 1:
                print(f"Break between {times_sorted[i]} and {times_sorted[i + 1]} is more than 1 hour")


print("Task4: get gaps")
get_long_breaks(2021, 4, 28, 30)

# 5. После перерасчёта оказалось, что для окупаемости, каждый день в кафе должно продаваться не меньше 20 чашек кофе.
# Надо написать декоратор, который будет проверять кол-во чашек кофе на каждый день. И если их было меньше 20,
# возвращать сообщение с ошибкой (подсказка: try/except).