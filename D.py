def seen_numbers(numbers_str):

  seen = {}
  results = []
  for number in numbers_str.split():
    number = int(number)
    if number in seen:
      results.append("YES")
    else:
      seen[number] = 1
      results.append("NO")
  return results

numbers_str = "1 2 3 2 3 4"
results = seen_numbers(numbers_str)
print("\n".join(results))
