#Decorator = A function that extends the behavior of another function
#w/o modifying the base function
#Pass the base function as an argument to the decorator
#by default a function need to focus on single task for reusability.


import time
from datetime import datetime, timedelta

#enhanced function
def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        end_time = time.time()
        task_time = end_time - start_time
        print(f"Task Time: {task_time} seconds")
        return result
    return enhanced_fn

#base function
@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} Tea...")
    time.sleep(steep_time)
    print("Tea is ready!")
@timer_dec
def brew_coffee():
    print("Brewing coffee...")
    time.sleep(2)
    print("Coffee is ready!")
    return f"Drink coffee by {datetime.now()+ timedelta(minutes=10)}"
#passing positional arguments *args
#brew_tea("ginger", 1)

#passing keyword arguments **kwargs
brew_tea(tea_type="ginger", steep_time=1)

print(brew_coffee())

