def find(s, n):
    # A dictionary to store the numbers we have seen so far
    # The key will be the number, and the value will be its index.
    # e.g., {2: 0, 7: 1, 11: 2}
    seen_numbers = {}

    # We use enumerate() to get both the index (i) and the value (num)
    # at the same time.
    for i, num in enumerate(s):
        # Calculate the "complement" - the other number we need to find
        # to reach the target 'n'.
        complement = n - num

        # Check if this complement is already in our dictionary
        if complement in seen_numbers:
            # If it is, we found our pair!
            # The current index is 'i', and the complement's index
            # is stored in our dictionary.
            return [seen_numbers[complement], i]
        
        # If the complement was NOT found, it means we haven't
        # found our pair yet.
        # We add the *current* number and its index to the dictionary
        # to be checked against in future loops.
        seen_numbers[num] = i

    # If we get through the whole loop without finding a pair,
    # return None as per your template.
    return None

# --- Example Usage ---
print("--- Efficient Hash Map (Dictionary) Solution ---")

# Example 1:
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"List: {nums1}, Target: {target1}")
print(f"Output: {find(nums1, target1)}") # Output: [0, 1]
print("-" * 20)

# Example 2:
nums2 = [3, 2, 4]
target2 = 6
print(f"List: {nums2}, Target: {target2}")
print(f"Output: {find(nums2, target2)}") # Output: [1, 2]
print("-" * 20)

# Example 3:
nums3 = [3, 3]
target3 = 6
print(f"List: {nums3}, Target: {target3}")
print(f"Output: {find(nums3, target3)}") # Output: [0, 1]
print("-" * 20)

# Example 4 (No solution):
nums4 = [1, 2, 3]
target4 = 10
print(f"List: {nums4}, Target: {target4}")
print(f"Output: {find(nums4, target4)}") # Output: None
print("-" * 20)
