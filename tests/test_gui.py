import time
import datetime
start_time = 0
end_time = 0
start_time = time.perf_counter()
end_time = time.perf_counter()
timer = end_time - start_time


print(timer)

# time = datetime.datetime.now()

# print(time.second)

# while True:
#     if time.second <= 10:
#         print(time.second)
#     else:
#         break