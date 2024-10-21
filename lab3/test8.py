from task8 import *

simulation(num_minutes=120, num_operators=3)

for operators in range(2, 6):
    print(f"\nСимуляция с {operators} операторами:")
    simulation(num_minutes=120, num_operators=operators)
