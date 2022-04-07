def push(stack, element):
  """
  Add value in to the stack
  """
  stack.append(element) # return something

def pop(stack):
  """
  Remove last value ever pushed
  """
  return print(stack.pop())

def peek(stack):
  """
  Print and show value what pops next
  """
  return print("peek value: {}".format(stack[-1]))

def is_empty(stack):
  """
  Check and print whether stack empty or not.
  """
  if len(stack)==0:
    print(True)
  else:
    print(False)


if __name__=='__main__':
  # 쉘에서 파일이 실행될 때 아래의 일을 합니다.
  # Stacking process

  stack_1 = [] # list: collection
  push(stack_1, 1)
  push(stack_1, 2)
  push(stack_1, 3)

  is_empty(stack_1)
  print(stack_1)
  peek(stack_1) #3

  pop(stack_1)
  pop(stack_1)
  pop(stack_1)
  is_empty(stack_1)