def isHappy(n): 
  sum = 0 
  looptest = {1, } 
  while(n!=1): 
    while(n>0): 
      sum = sum + (n%10)*(n%10) 
      n = n // 10 
    n = sum 
    if(n in looptest): 
      break 
    looptest.add(n) 

    sum = 0 
  if(n == 1): 
    return True; 
  else: 
    return False; 

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt",  "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
        print("Results saved to /app/bind_mount/output.txt")