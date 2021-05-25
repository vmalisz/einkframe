from datetime import datetime,time

def main():
	print('start')
	now = datetime.time(datetime.now())
	print(r''+str(now))
	#print(time_in_range(str(now)))
	print(time_in_range(now))

def time_in_range(x):
    """Return true if x is in the range [start, end]"""
    #start =  datetime.time(datetime(2020,5,16,5,0))
    start = time(5,0,0)
    end =  time(22,0,0)
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

if __name__ == '__main__':
   main()