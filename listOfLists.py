#Mia Escoto 
#List of lists challenge 

Universities = [
  ['CIT', 2175, 37704], 
  ['Harvard', 19627, 39849], 
  ['MIT', 10566, 40732], 
  ['Princeton', 7802, 37000], 
  ['Rice', 5879, 35551],
  ['Stanford', 19535, 40569],
  ['Yale', 11701, 40500],
]


def enrollment_stat(WholeList):
  total_students = []
  total_tuition = []
  for list in WholeList:
    total_students.append(list[1])
    total_tuition.append(list[2])
  
  return total_students, total_tuition
  


def mean(list):
  mean = 0
  for i in range(len(list)): 
    mean += list[i]
  mean /= len(list)
  return round(mean,2)

def median(list):
  list.sort()
  median = list[int((len(list))/2)]
  return median 

print(f"Total Students:   {sum(enrollment_stat(Universities)[0])}")
print(f"Total Tuition   {sum(enrollment_stat(Universities)[1]):,}")
print("\n")
print(f"Student Mean:   {mean(enrollment_stat(Universities)[0]):,}")
print(f"Student Median:   {median(enrollment_stat(Universities)[0]):,}")
print("\n")
print(f"Tuitions Mean:   {mean(enrollment_stat(Universities)[1]):,}")
print(f"Tuitions Median:   {median(enrollment_stat(Universities)[1]):,}")