import random


def main():
  test_dict = {}
  path = "dict_1.txt"
  file = open(path, "r")
  dict = file.read()
    
  """for line in dict:
      (key, val) = line.split(" : ")
      test_dict[key] = val"""
  print(dict)
  file.close()

if __name__ == "__main__":
  main()
