import numpy

speed1=[86,87,88,86,87,85,86]
speed2=[32,111,138,28,59,77,97]

mean_test=numpy.mean(speed1)
low_std_test=numpy.std(speed1)
print("speed1s' within Low_Standard_Deviation,", low_std_test)
print("from Mean_value,", mean_test, "\n")

mean_test=numpy.mean(speed2)
high_std_test=numpy.std(speed2)
print("speed2s' within High_Standard_Deviation,", high_std_test)
print("from Mean_value,", mean_test)
