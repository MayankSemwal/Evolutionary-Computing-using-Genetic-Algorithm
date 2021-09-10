# Evolutionary-Computing-using-Genetic-Algorithm
Design and implement of Genetic algorithm for keystroke detection

KEYSTROKE DETECTOR: Steps to design and implement anomaly detector.
1. Initialization: Read the csv file and store it into data frame using pandas.Discard all the down-down (excluding return key) key values because it’s the sum of hold and up-down key values and consider h and ud (i.e. 21 columns).
2. Evaluation: Detector will take 10 keystroke login samples per user and generate keystroke signature for this user in which imposter set (250 records, 5 per imposter, 50 imposters in all). In next step, data will be trained using their mean and std vector are calculated and outliers will be removed by taking into account deviations in typing habits. To reject the outliers first Euclidean distance between training and mean vector is calculated and any vector whose distance is greater than 3 times the standard vector. Pass the test samples, imposter set and results of training function i.e. mean and std values into testing function, it will calculate the Euclidean distance between test sample and mean vector. Having obtained the scores for both kind of samples, genuine and imposter, in lists user
scores and imposter scores respectively, we evaluate the equal error rate (EER) for the detector. Two types of detector we have used: Hybrid Manhattan (used Euclidean dist. to train samples, drop the outliers and test the samples with Manhattan dist.) and Euclidean distance
3. Performance Analysis: In total each user will be tested 700 times (10*50+200) for user’s authenticity and will be repeated for all 51 users.

BIOMETRIC ADVERSARY FRAMEWORK: Steps to design and implement of Genetic algorithm.
• Initialization: We have created an initial population in the shape of an array of fix size and can be any
desired size from few individuals to many.
• Fitness Function: Each member of the population is evaluated and we calculate a fitness for each
individual. The fitness value is calculated using Euclidian distance ((math.sqrt(mean-initialpop
)**2)/standard_deviation). If Euclidean distance is greater than or equal to 0.85, value will be appended
to fitness array and will be returned.
• Selection: It is used to select n number of parents (we have considered two parents). To improve
population’s overall fitness. We have considered one parent to be randomly selected from fitness array
and other parent randomly from the initial population, the basic idea is to diversify selection of parents
but also considering single parent to be selected from the best fitted results.
• Crossover: During crossover we create new individuals (known as offsprings) by combining aspects of
our selected parents. The crossover rate is the probability of acceptance to select individuals of next
generation which is 0.5 (i.e. 50%) in our crossover criteria. We have used single point cross-over in which
parent to the right of that point are swapped between the two parents. This result in two offsprings each
carrying some genetic information from parents.
• Mutation: To add a little bit randomness into our population genetics because every combination of
solution will be different from initial population. We have used a random value generated in each
generation ranging from 0 to 0.5 to be added to offspring.
• Repeat: Now, we have our next generation we can start again from fitness until we reach a termination
condition.
• Termination: If mutation result is greater than or equal to maximum from fitness result array (i.e.
fitnessArr.max ()) the generation will break and display the set of best mutations in each generation into
an array, out of which we will select the maximum two compare with maximum from fitness array.
• Goal: The goal is to get mutation results close to the fitness value.
