# Variable types
x = 10        # int
y = 3.5       # float
z = "25"      # str

# Operators
sum_val = x + y   # Arithmetic
check = x > y     # Comparison
logic = (x > 5) and (y < 10)  # Logical

# Type Conversion
implicit = x + y        # int + float → float (implicit)
explicit = x + int(z)   # str → int (explicit)

print("Sum:", sum_val, type(sum_val))
print("Check:", check)
print("Logic:", logic)
print("Implicit:", implicit, type(implicit))
print("Explicit:", explicit, type(explicit))
