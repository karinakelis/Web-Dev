def sleep_in(weekday, vacation):
    return not weekday or vacation

# Test cases
print(sleep_in(False, False))  # Should print: True
print(sleep_in(True, False))   # Should print: False
print(sleep_in(False, True))   # Should print: True