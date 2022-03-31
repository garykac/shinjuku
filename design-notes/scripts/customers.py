# Customer draw probabilities

from __future__ import division  # So that / performs float division

import copy
import numpy
import random

_customer_types = {
    'f': 23,#20,    # Food
    'c': 20,#17,    # Clothing
    'b': 16,#13,    # Books
    'e': 13,#10,    # Electronics (Video games)
}

_customer_names = {
    'f': 'Food',
    'c': 'Clothing',
    'b': 'Books',
    'e': 'Electronics',
}

_customer_order = 'fcbe'

def almost_equals(a,b):
    return (a + 0.00001) > b and (a - 0.00001) > b

def remove_ith(str, index):
    if index == 0:
        return str[index+1:]
    return str[:index-1] + str[index:]

# Given a |seq| of customers, create a dict with the count of each type.
def count_types(seq):
    count = {}
    for c in seq:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

class CustProb():
    def __init__(self):
        self.num_total = 0
        for t in _customer_types:
            self.num_total += _customer_types[t]
        
        self.customers = ['']
        self.num_customers_added = 0
        self.probs = {}

    # Expand the list of possible customer sequences by adding one of each type to
    # each of the current sequences.
    def add_customers(self):
        result = []
        for c in self.customers:
            for t in _customer_types:
                result.append(c+t)
        self.customers = result
        self.num_customers_added += 1

    # Calc probabilities for all the possible customer sequences.
    def calc_probs(self):
        self.probs = {}
        total_probs = 0.0
        for c in self.customers:
            p = self.calc_prob(c)
            self.probs[c] = p
            total_probs += p
        if almost_equals(total_probs, 1.0):
            print('ERROR expect probs to sum to 1, got', total_probs)
        #print(total_probs)
    
    # Given a |seq| of customers, calc the probability of that sequence occuring.
    def calc_prob(self, seq):
        total = self.num_total
        types = copy.deepcopy(_customer_types)
        prob = 1.0
        for i in range(0, len(seq)):
            type = seq[i]
            count = types[type]
            prob *= (count / total)
            types[type] -= 1
            total -= 1
        return prob
    
    # Count how many instances of |num_copies| duplicates in the counts.
    # Of the non-matches, the number of single types must be |num_singles|.
    def count_copies(self, counts, num_copies, num_singles):
        num = 0
        singles = 0
        for c in counts:
            if counts[c] == num_copies:
                num += 1
            elif counts[c] == 1:
                singles += 1
        if singles != num_singles:
            return 0
        return num

    # Sum the probability of all events matching the given criteria.
    # |check| - only run this if there are at least |check| customers
    # |title| to display for this check
    # |count| - how big of a group are we checking for? (2 = doubles, 3 = triples)
    # |num_copies| - how many distinct groups? (1 = exactly 1 group)
    # |num_singles| - how many remaining ungrouped customers?
    def sum_matching_prob(self, check, title, count, num_copies, num_singles):
        prob = 0.0
        if self.num_customers_added >= check:
            print(' %s:' % title, end='')
            for c in self.customers:
                counts = count_types(c)
                if self.count_copies(counts, count, num_singles) == num_copies:
                    prob += self.probs[c]            
            print(prob, end='')
        return prob
            
    def print_customers(self):
        self.calc_probs()
        print('After', self.num_customers_added, 'customers:')
        p = 0.0
        n = self.num_customers_added

        p += self.sum_matching_prob(1, 'All different', 1, n, 0)

        p += self.sum_matching_prob(2, 'Doubles', 2, 1, n-2)

        p += self.sum_matching_prob(3, 'Triples', 3, 1, n-3)

        p += self.sum_matching_prob(4, 'Doubles x2', 2, 2, n-4)
        p += self.sum_matching_prob(4, '4-match', 4, 1, n-4)

        print(' Total:', p)

class MonteCarloProb():
    def __init__(self):
        self.num_total = 0
        self.initial_set = ''
        for t in _customer_types:
            self.num_total += _customer_types[t]
            self.initial_set += t * _customer_types[t]

        self.verbose = True

        self.reset_simulation()

        self.num_sims = 0
        self.total_turns = 0
        self.total_clumps = {}
        
        self.data_turns = []
        self.data_clump = {}
        self.data_clump_percent = {}

    def reset_simulation(self):
        # The next locations where the customers will be placed.
        self.cards = ['', '', '', '']

        # The bag of customers to draw from
        self.bag = copy.deepcopy(self.initial_set);
        self.num_customers = self.num_total
        
        self.sim_turns = 0
        self.sim_clumps = {}
        
    def set_verbosity(self, v):
        self.verbose = v
        
    # Remove a single customer from the bag at random and return the type (as a char).
    def draw_customer(self):
        if self.num_customers < 1:
            return ''
        index = random.randint(0, self.num_customers-1)
        cust = self.bag[index]
        self.bag = remove_ith(self.bag, index+1)
        self.num_customers -= 1
        return cust
                
    # Draw |count| customers from the bag and return a string with the customers drawn.
    def draw_customers(self, count):
        c = ''
        for x in range(0, count):
            c += self.draw_customer()
        return c

    # Place the given customers onto the cards.
    def place_customers(self, customers):
        counts = count_types(customers)
        
        # If there are already customers on the cards, add any matching ones.
        for i in range(0, len(self.cards)):
            if self.cards[i] == '':
                continue
            type = self.cards[i][0]
            if type != '' and type in counts:
                self.cards[i] += type * counts[type]
                del counts[type]
        
        # Add remaining customers to new cards.
        for type in _customer_types:
            if type in counts:
                # Find next empty card.
                for i in range(0, len(self.cards)):
                    if self.cards[i] == '':
                        self.cards[i] = type * counts[type]
                        break

    # Remove the next card (to simulate placing customers onto map).
    def remove_card(self):
        self.cards.append('')
        customers = self.cards.pop(0)
        clump_size = len(customers)
        if clump_size != 0:
            if clump_size in self.sim_clumps:
                self.sim_clumps[clump_size] += 1
            else:
                self.sim_clumps[clump_size] = 1
        return customers
            
    # Simulate pulling |count| customers at a time.
    def run_simulation(self, count):
        self.reset_simulation()
        next_draw = count

        # Draw customers from bag until none are left.
        done = False
        while not done:
            customers = self.draw_customers(next_draw)
            if customers == '':
                done = True
                if self.verbose:
                    print('Last customer drawn')
                continue
            self.sim_turns += 1
            if self.verbose:
                print('Sim turn', self.sim_turns)
            #print(customers, self.bag)
            self.place_customers(customers)
            if self.verbose:
                print(' Placing', customers, 'onto cards:', self.cards, '(%d) remaining' % len(self.bag))
            map_customers = self.remove_card()
            if self.verbose:
                print(' Moving customers to map:', map_customers)
            # Next draw should replace the customers on the cards.
            # There should always be |count| customers on the cards.
            next_draw = len(map_customers)

        # Any customers left on cards need to be placed on map.
        done = False
        while not done:
            map_customers = self.remove_card()
            if map_customers == '':
                done = True
                continue
            self.sim_turns += 1
            if self.verbose:
                print('Sim turn', self.sim_turns)
                print(' Moving customers to map:', map_customers)
        
    def record_simulation(self):
        sturns = self.sim_turns
        self.total_turns += sturns
        self.data_turns.append(sturns)

        # Record the percentage of turns for each clump size.
        for clump_size in self.sim_clumps:
            if not clump_size in self.data_clump:
                self.data_clump[clump_size] = 0
                self.data_clump_percent[clump_size] = []
            self.data_clump[clump_size] += self.sim_clumps[clump_size]
            self.data_clump_percent[clump_size].append(self.sim_clumps[clump_size]/sturns)
        self.num_sims += 1
        #print(self.sim_turns, self.sim_clumps)
        
    def run_simulations(self, cust_count, sim_runs):
        for x in range(0, sim_runs):
            self.run_simulation(cust_count)
            self.record_simulation()

    def summary(self, cust_count):
        print('Customer distribution:')
        for c in list(_customer_order):
            print('  ', _customer_types[c], _customer_names[c])
        print(cust_count, 'customers drawn per turn')
        print('Number of simulations:', self.num_sims)
        average = self.total_turns / self.num_sims
        sd = numpy.std(self.data_turns)
        #print('Avg number of turns:', average, 'stddev:', sd)
        print("Avg number of turns {0:5.2f} stddev {1:4.2f}".format(average, sd))

        print('Size of customer clumps placed on map each turn:')
        avg_cust = 0
        for clump_size in sorted(self.data_clump.keys()):
            percent = self.data_clump[clump_size] / self.total_turns
            sd = numpy.std(self.data_clump_percent[clump_size])
            #print(clump_size, percent, 'stddev:', sd)
            print("   {0} - {1:5.2f}% stddev {2:4.2f}".format(clump_size, percent * 100, sd * 100))
            avg_cust += clump_size * percent
        print("Average clump size: {0:5.2f}".format(avg_cust))

def static_check():
    print()
    print('*** Static check ***')
    prob = CustProb()

    for x in range(0,4):
        prob.add_customers()
        prob.print_customers()

def monte_carlo_check():
    print()
    print('*** Monte Carlo check ***')
    prob = MonteCarloProb()
    
    customer_count = 8
    
    prob.set_verbosity(False)
    prob.run_simulations(customer_count, 1000)
    prob.summary(customer_count)
    
#static_check()
monte_carlo_check()
