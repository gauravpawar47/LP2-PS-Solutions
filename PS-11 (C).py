class AirlineSchedulingExpertSystem:
    def __init__(self):
        # Aircraft types and their respective capacities
        self.aircrafts = {
            'A320': {'capacity': 150, 'type': 'Passenger'},
            'B737': {'capacity': 180, 'type': 'Passenger'},
            'CARGO747': {'capacity': 300, 'type': 'Cargo'},
            'CARGO777': {'capacity': 250, 'type': 'Cargo'}
        }
        self.flight_schedules = {}

    def schedule_flight(self, aircraft_id, flight_time, flight_type, cargo_weight=0):
        if aircraft_id not in self.aircrafts:
            print(f"Error: Aircraft {aircraft_id} not found. Please select a valid aircraft.")
            return

        aircraft = self.aircrafts[aircraft_id]

        # Validate aircraft type for the flight type
        if flight_type == 'Cargo' and aircraft['type'] != 'Cargo':
            print(f"Error: Aircraft {aircraft_id} is not suitable for Cargo flights.")
            return

        # Check if the cargo weight exceeds the aircraft's capacity
        if flight_type == 'Cargo' and cargo_weight > aircraft['capacity']:
            print(f"Error: Cargo weight exceeds the aircraft's capacity of {aircraft['capacity']} kg.")
            return

        # Schedule the flight
        self.flight_schedules[flight_time] = {
            'aircraft_id': aircraft_id,
            'flight_type': flight_type,
            'cargo_weight': cargo_weight if flight_type == 'Cargo' else 0
        }

        print(f"Flight successfully scheduled: Aircraft {aircraft_id} for {flight_type} at {flight_time}.")

    def view_schedule(self):
        print("\nCurrent Flight Schedules:\n")
        if not self.flight_schedules:
            print("No flights scheduled yet.")
        for flight_time, details in self.flight_schedules.items():
            print(f"At {flight_time}: {details['aircraft_id']} for {details['flight_type']} (Cargo Weight: {details['cargo_weight']} kg)")
            print("-" * 50)

# Example usage
def airline_scheduling():
    print("Welcome to the Airline Scheduling and Cargo Expert System\n")
    expert_system = AirlineSchedulingExpertSystem()
    
    while True:
        aircraft_id = input("Enter aircraft ID (A320, B737, CARGO747, CARGO777) or 'exit' to quit: ").strip()
        if aircraft_id.lower() == 'exit':
            break
        
        flight_time = input("Enter flight time (e.g., 2025-05-08 10:00): ").strip()
        flight_type = input("Enter flight type (Passenger or Cargo): ").strip()

        cargo_weight = 0
        if flight_type.lower() == 'cargo':
            cargo_weight = int(input("Enter cargo weight (in kg): "))
        
        expert_system.schedule_flight(aircraft_id, flight_time, flight_type, cargo_weight)
    
    expert_system.view_schedule()

airline_scheduling()
