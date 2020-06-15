# Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
# The equation has 6 inputs (x1 to x6) and 6 weights (w1 to w6) as shown
# inputs values are (x1,x2,x3,x4,x5,x6)=(4,-2,7,5,11,1).
# find the parameters (weights) that maximize such equation
import numpy
import GA
# Inputs of the equation.
equation_inputs = [4, -2, 3.5, 5, -11, -4.7]
# Number of the weights we are looking to optimize.
num_weights = 6

solution_per_population = 8
# Defining the population size.
population_size = (solution_per_population, num_weights)
# Creating the initial population
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=population_size)
print("---New Population---\n {}".format(new_population))
num_generations = 1

num_parents_mating = 4
for num_generations in range(num_generations):
    # Measuring the fitness of each chromosome in the population
    fitness = GA.cal_population_fitness(equation_inputs, new_population)
    print("---Fitness---\n {}".format(fitness))
    # Selecting the best parents in the population for mating
    parents = GA.select_mating_pool(new_population, fitness, num_parents_mating)
    print("---Best parents---\n {}".format(parents))
    # Generating next generation using crossover
    offspring_crossover = GA.crossover(parents, offspring_size=(population_size[0] - parents.shape[0], num_weights))
    # Adding some variations to the offspring using mutation.
    offspring_mutation = GA.mutation(offspring_crossover)
    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

