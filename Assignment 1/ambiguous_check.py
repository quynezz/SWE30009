def original_program(A, B):
    A = A - B
    C = A * 2
    return C

def is_ambiguous(A, B):
    orig_result = original_program(A, B)
    # Generate incorrect results by applying various operations to A and B
    incorrect_results = [(A + B) * 2, (A * B) * 2, (A / B) * 2, 
                         A - B + 2, A - B - 2, (A - B) / 2, 
                         (A + B) + 2, (A * B) + 2, (A / B) + 2, 
                         (A + B) - 2, (A * B) - 2, (A / B) - 2, 
                         (A + B) / 2, (A * B) / 2, (A / B) / 2]
    # Check if any of the incorrect results match the original result
    return any(orig_result == result for result in incorrect_results)
# Given B value
B = 1
# Initialize a list to store ambiguous A values
ambiguous_A_values = []
# Iterate through a range of A values from -100 to 100
for A in range(-100, 101):
    # Check if the current A value is ambiguous for the given B value
    if is_ambiguous(A, B):
    # If ambiguous, add the current value to the list of ambiguous A values
        ambiguous_A_values.append(A)
# Print the ambiguous A values for B=1
print("Ambiguous A values for B=1 are:", ambiguous_A_values) 
#  1
