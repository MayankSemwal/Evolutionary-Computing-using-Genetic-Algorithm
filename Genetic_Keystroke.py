import numpy
import random
# import math


# Calculate the fitness of population
def FitnessFunction(Population_array):
    calculation = []
    fitness = []
    for calc in Population_array:
        calculation.append(calc)
    mean_vector = numpy.mean(calculation)
    std_vector = numpy.std(calculation)

    for pop in Population_array:
        # Manhattan function
        cur_sc = abs(mean_vector - pop) / std_vector
        # Euclidean function
        # cur_sc = math.sqrt((mean_vector - pop) ** 2) / std_vector
        if cur_sc >= 0.85:
            fitness.append(cur_sc)  # Append values from population if they are more than 0.85
    return numpy.array(fitness)


# Select number of parents from population(i.e. 2 parents in this program)
# select parents randomly from fitness values and initial population
def ParentSelection(init_pop, get_fitness, num_parents):
    SelectParents = numpy.empty(num_parents, numpy.float32)
    for i in range(num_parents - 1):
        for j in range(num_parents - 1):
            parent_a = numpy.max(get_fitness)  # from fitness array
            parent_b = random.choice(init_pop)
            SelectParents[i] = parent_a
            SelectParents[j] = parent_b
    return SelectParents


# On the basis of number of parents function will create n number of offsprings.
def Crossover(parents, offspring_size):
    # The point at which crossover takes place between two parents. Usually, it is at the center.
    offspring = numpy.empty(offspring_size, numpy.float32)
    for k in range(offspring_size):
        check_cross_rate = numpy.random.uniform(0, 1, 1)
        if check_cross_rate <= CROSS_RATE:
            objparent1 = k % parents.shape[0]   # Index of the first parent to mate.
            objparent2 = (k + 1) % parents.shape[0]  # Index of the second parent to mate.
            offspring[k] = parents[objparent1]
            offspring[k] = parents[objparent2]
    return offspring


def Mutation(offspring_crossover, num_mutations):
    # Mutation changes a number of genes as defined by the
    # num_mutations argument. The changes are random.
    for idx in range(offspring_crossover.shape[0]):
        check_mutation_rate = numpy.random.uniform(0, 0.009, 1)
        if check_mutation_rate <= MUTATION_RATE:
            for mutation_num in range(num_mutations):
                random_value = numpy.random.uniform(0, 0.5, 1)   # The random value to be added to the gene.
                offspring_crossover[idx] = offspring_crossover[idx] + random_value
    return offspring_crossover


mutation_array = []

CROSS_RATE = 0.5      # mating probability
MUTATION_RATE = 0.003   # mutation probability
N_GENERATIONS = 10


# Initial Population
Population_array = [0.665, 0.5423, 0.6744, 0.3432, 0.6523, 0.9612, 0.4387, 0.7609, 0.8991, 0.4512, 0.253, 0.981, 1.32]
# Population_array = numpy.array(population)

for generation in range(N_GENERATIONS):
    print("Generations :", generation)
    get_fitness = FitnessFunction(Population_array)

    # Selecting the best parents in the population for mating.
    parents = ParentSelection(Population_array, get_fitness, num_parents=2)
    print("Parents")
    print(parents)

    # Generating next generation using crossover.
    offspring_crossover = Crossover(parents, offspring_size=parents.shape[0])
    print("Crossover")
    print(offspring_crossover)

    # Adding some variations to the offspring using mutation.
    offspring_mutation = Mutation(offspring_crossover, num_mutations=offspring_crossover.shape[0])
    mutation_array.append(offspring_mutation)
    print("Mutation")
    print(offspring_mutation)
    print()

    mutation_result = offspring_mutation.max()
    fitness_result = get_fitness.max()


    def Add_To_InitialPop(mutations, no):  # Function to select first 50 % records
        for k in range(no - 1):
            obj = k % mutations.shape[0]
            output = mutations[obj]
        return output

    # Add 50 percentage mutations into initial populations
    Mutation_to_Pop = Add_To_InitialPop(offspring_mutation, offspring_mutation.shape[0])
    Population_array.append(Mutation_to_Pop)

    # Termination condition (if mutation result is greater than or equal to maximum value from fitness result)
    if mutation_result >= fitness_result:
        break


mutation_array = numpy.array(mutation_array)

get_fitness = numpy.array(Population_array)

best_match_idx = numpy.where(get_fitness == numpy.max(get_fitness))

best_match_idx1 = numpy.where(mutation_array == numpy.max(mutation_array))

print()
print("Best Mutations: ", mutation_array.max(axis=1))
print()
print("Best solution from mutations: ", mutation_array[best_match_idx1])
print()
print("Best solution from fitness : ", get_fitness[best_match_idx])