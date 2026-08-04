time = int(input("Enter the time in minutes: "))

hours = time // 60
minutes = time % 60

print(f"Time: {time} minutes")
print(f"{hours} hours and {minutes} minutes")