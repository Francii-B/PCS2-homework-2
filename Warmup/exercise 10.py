#Exercise 10: Calendar convertion
import sys


def timeConversion(s):
    time={'P':['13','14','15','16','17','18','19','20','21','22','23','12'], #PM
          'A':['01','02','03','04','05','06','07','08','09','10','11','00'] } #AM
    d=s[-2] #check whether the time is PM or AM
    hh=s[:2] #extract the hour
    return time[d][int(hh)-1] + s[2:-2] #pick the right hour from the dictionary adding the minutes and the seconds present in s the string



s = input().strip()
result = timeConversion(s)
print(result)
