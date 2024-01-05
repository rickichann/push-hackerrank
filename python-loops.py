if __name__ == '__main__':
    n = int(input())
    
    def py_loops(n):
    # constraint
      if n >= 1 and n <= 20:
            for i in range(n):
                  print(i**2)

    py_loops(n)
    