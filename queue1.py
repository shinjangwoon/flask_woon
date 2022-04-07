from collections import deque


def enqueue(queue, element):
  """
  Add element at last of deque
  """
  queue.append(element)

def dequeue(queue):
  """
  Remove element from 1st position of deque
  """
  print(queue.popleft())

def front(queue):
  print(queue[0])

def is_empty(queue):
  '''
  return True if queue is empty, otherwise return False
  '''
  if len(queue)==0:
    print(True)
    return(True)
  else:
    print(False)
    return(False)
    
    

if __name__=='__main__':
  queue_1 = deque()

  enqueue(queue_1, 1)
  enqueue(queue_1, 2)
  enqueue(queue_1, 3)

  print(queue_1)

  dequeue(queue_1)
  dequeue(queue_1)
  dequeue(queue_1)
  
  print(queue_1)