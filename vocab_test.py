import random


def open_dict(path):
  dict_o = {} 
  with open(path, "r", encoding='utf-8') as file:
    for line in file:
        key, val = line.strip().split(" : ")
        dict_o[key] = val
  return(dict_o)
  
def main():
  selected_dict = "dict_1.txt"
  test_dict = open_dict(selected_dict)
  print(test_dict)

if __name__ == "__main__":
  main()
