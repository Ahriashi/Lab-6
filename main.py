def main():
  count = int(input("Введите колличество критериев: "))
  nums = [[0 for j in range(count)] for i in range(count)]
  for i in range(count):
    for j in range(count):
      if i == j:
        nums[i][j] = 1
      elif i < j:
        while True:
          nums[i][j] = float(input(f"Введите коэфициент сравнения {i+1} s {j+1}(ot 0 do 9): "))
          if nums[i][j] > 9 or nums[i][j] <= 0:
            print("Недопустимое значение, попробуйте ещё раз\n")
          else:
            break
  for i in range(count):
    for j in range(count):
      if i > j:
        nums[i][j] = 1 / nums[j][i]

  vec = []
  sum = 0
  print("Итоговая матрица:")
  for i in range(count):
    for j in range(count):
      print(f"{nums[i][j]:.2f}  ", end="")
      sum += nums[i][j]
    vec.append(sum)
    sum = 0
    print()
  for i in range(count):
    sum += vec[i]
  print("Весовые коэфициенты: ", end="")
  for i in range(count):
    print(f"{i+1} - {vec[i]/sum:.2f}, ", end="")

if __name__ == "__main__":
  main()
