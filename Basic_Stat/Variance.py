# Variance - Calculated as the sum of squared distances from each point to the mean
# There is a difference between the Sample Variance and Population Variance, Subject To Bessele's Correction (N-1)


def calculate_mean(samples):
    return sum(samples)/len(samples)


# Sample Variance  = sum(x-mean)**2 / N-1
sample_population = [4, 7, 9, 8, 11]
mean = calculate_mean(sample_population)
variance = sum([(sample-mean)**2 for sample in sample_population])/(len(sample_population)-1)
print("Sample Variance : ", variance)


# Population Variance = sum(x-mean)**2 / N
complete_population = [4, 7, 9, 8, 11]
mean = calculate_mean(complete_population)
variance = sum([(sample-mean)**2 for sample in sample_population])/len(sample_population)
print("Population Variance : ", variance)
