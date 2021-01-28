from _typeshed import HasFileno, SupportsLessThan
import pandas

mydataset  = {'Instruments':["Guitar", "Recorder", "Violin", "Piano", "Flute"], 'level out of 5':["4","2","1","2","1"]}

myvar = pandas.DataFrame(mydataset)

print(myvar)
