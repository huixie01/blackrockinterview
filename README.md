# blackrockinterview

Question 1:
Given two inputs: operationlist, datalist where data is integer and operation is push or pop
Write a function minMax(operationlist, datalist) in python and return a list with element value = min*max of the datalist in each iterative operation.

For example,
  given operationlist = [push, push, push, pop] and datalist=[1,2,3,1]
  The function minmax shall implement the following:
  1. initialize an empty element list []
  2. push the first data into list [1]
  3. calculate the min and max of the list 1*1=1
  4. put 1 into te return list[1]
  5. push the second data into list [1 ,2 ]
  6. The list shall be in the order
  7. calculate the min and max of the list 1*2 = 2
  8. put 2 into the return list [1, 2]
  9. push the third data into list [1,2,3]
  10.calculate the min and max of the list 1*3 = 3
  11. put 4 into the return list [1,2,3]
  12.pop the data [1] from list [2,3]
  13.calculate the min and max of the list 2*3=6
  14. return [2,3,6]
  
