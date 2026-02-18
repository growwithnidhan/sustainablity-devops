# carbon_check.py
import random
import sys

# simulate carbon intensity (0 = clean, 100 = very dirty)
carbon_intensity = random.randint(0, 100)
print(f"Current carbon intensity: {carbon_intensity}")

# if high, stop the build
if carbon_intensity > 70:
    print("High carbon intensity detected! Pausing build.")
    sys.exit(1)
else:
    print("Carbon intensity is acceptable. Proceeding with build.")
