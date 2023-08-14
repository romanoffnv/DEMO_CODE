import re

input_string = 'Mercedes-Benz C-Class У798ОН799, #Е797СО120О33'
pattern = r'^([\w\s-]+)'  # This pattern captures words, spaces, and hyphens

match = re.match(pattern, input_string)
if match:
    extracted_substring = match.group(1)
    print(extracted_substring)
else:
    print("Pattern didn't match")