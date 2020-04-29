import random
import statistics
import time
import simpy

wait_times = []

class Theater(object):

    # env = simpy.Environment()

    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1,3))
    
    def check_ticket(self, moviegoer):
        yield self.env.timeout(3/60.0)

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(1,5))

def go_to_movies(env, moviegoer, theater):
    arrival_time = env.now

    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.purchase_ticket(moviegoer))

    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(moviegoer))

    if(random.choice([True, False])):
        with theater.server.request() as request:
            yield request
            yield env.process(theater.check_ticket(moviegoer))
    
    wait_times.append(env.now - arrival_time)

def run_theater(env, num_cashiers, num_servers, num_ushers):
    theater = Theater(env, num_cashiers, num_servers, num_ushers)
    
    # Starting with some moviegoers already in line
    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, theater))

    # Processing the rest of the moviegoers who arrive at set time intervals
    while(True):
        yield env.timeout(12/60.0)

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, theater))

# Calculate average wait time
def get_average_wait_time(wait_times):
    average_wait_time = statistics.mean(wait_times)


def calculate_wait_time(wait_times):
    average_wait_time = statistics.mean(wait_times)
    # Pretty print the results
    minutes, frac_minutes = divmod(average_wait_time, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("Input # of ushers working: ")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. The simulation will use default values:",
            "\n1 cashier, 1 server, 1 usher.",
        )
        params = [1, 1, 1]
    return params

def run_simulation(num_cashiers, num_servers, num_ushers):
    random.seed(42)
    wait_times.clear()
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=90)

    env = None

    return calculate_wait_time(wait_times)

def main():
    # Setup
    random.seed(time.time())
    num_cashiers, num_servers, num_ushers = get_user_input()

    # Run the simulation
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=500)

    # View the results
    mins, secs = calculate_wait_time(wait_times)
    print(
        "Running simulation...",
        "\nThe average wait time is {} minutes and {} seconds.".format(mins, secs),
    )


# main()
