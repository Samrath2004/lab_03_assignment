class FlightTable:
    def __init__(self):
        self.data = []

    def add_flight(self, p_id, process, start_time_ms, priority):
        self.data.append({
            'P_ID': p_id,
            'Process': process,
            'Start Time (ms)': start_time_ms,
            'Priority': priority
        })

    def sort_by_p_id(self):
        self.data.sort(key=lambda x: x['P_ID'])

    def sort_by_start_time(self):
        self.data.sort(key=lambda x: x['Start Time (ms)'])

    def sort_by_priority(self):
        priority_order = {'Low': 0, 'MID': 1, 'High': 2}
        self.data.sort(key=lambda x: priority_order[x['Priority']])

    def print_table(self):
        for row in self.data:
            print(f"P_ID: {row['P_ID']}, Process: {row['Process']}, Start Time (ms): {row['Start Time (ms)']}, Priority: {row['Priority']}")


if __name__ == "__main__":
    flight_table = FlightTable()

    flight_table.add_flight('P1', 'VSCode', 100, 'MID')
    flight_table.add_flight('P23', 'Eclipse', 234, 'MID')
    flight_table.add_flight('P93', 'Chrome', 189, 'High')
    flight_table.add_flight('P42', 'JDK 9', 9, 'High')
    flight_table.add_flight('P9', 'CMD', 7, 'High')
    flight_table.add_flight('P87', 'NotePad', 23, 'Low')

    while True:
        print("\nOptions:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flight_table.sort_by_p_id()
            flight_table.print_table()
        elif choice == '2':
            flight_table.sort_by_start_time()
            flight_table.print_table()
        elif choice == '3':
            flight_table.sort_by_priority()
            flight_table.print_table()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
