import sqlite3

DATABASE = 'cars.db'

def print_all_cars():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM car;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

        for car in results:
            print(f"Car: {car[1]} Top Speed : {car[2]}")

if __name__ == "__main__":
    print_all_cars()