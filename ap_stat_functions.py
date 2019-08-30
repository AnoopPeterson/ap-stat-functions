def mode(data : list):
	pass

def mean(data : list):
	return sum(data)/len(data)

def median(data : list):
	data = sorted(data)
	if(len(data) % 2 == 0): #If number of datapoints is even
		wanted_index = int(len(data)/2)
		sum_ = (data[wanted_index] + data[wanted_index - 1]) / 2
		return sum_

	else:
		wanted_index = int(len(data)/2)
		return data[wanted_index]

def std_dev(data : list):
	the_mean = mean(data)
	sum_ = 0
	for entry in data:
		diff = pow((entry - the_mean), 2)
		sum_ += diff
	sum_ /= (len(data) - 1)
	return sum_

def variance(data : list):
	return pow(std_dev(data), 2)

def quartiles(data : list):

	data = sorted(data)
	if len(data) % 2 == 0:
		lower_half = data[:int(len(data)/2)]
		upper_half = data[int(len(data)/2):]
		lower_med = median(lower_half)
		upper_med = median(upper_half)

		return (lower_med, upper_med)
	else:
		med = median(data)
		lower_half = data[:data.index(med) + 1]
		upper_half = data[data.index(med):]
		lower_med = median(lower_half)
		upper_med = median(upper_half)

		return (lower_med, upper_med)

def iqr(data : list):
	q1, q3 = quartiles(data)
	return q3 - q1

def outliers(data : list):
	q1, q3 = quartiles(data)
	range_ = iqr(data)
	q1_range = q1 - (1.5 * range_)
	q3_range = q3 + (1.5 * range_)
	outliers = [entry for entry in data if entry < q1_range or entry > q3_range]
	return outliers


data = [1,2,3,4,5]

print('mean ', mean(data))
print('std_dev ', std_dev(data))
print('variance', variance(data))

print('median ', median(data))
print('quartiles ', quartiles(data))
print('IQR ', iqr(data))
print('outliers ', outliers(data))