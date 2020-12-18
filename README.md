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
  
 Question 2:
  Create a visual model that explains list insertion.
  Text field: A field to provide input for inserting a new element into the list
  Button named as "Insert": Clicking this button inserts a new element at the end of the existing list, 
  the new element being the value provided in the text field.
  
  Requirements:
  No element should be inserted if the text field is empty. When the user clicks the button in case of empty input, display the alert
  with the message "please provide the valid input".
  When an element is inserted, reset the input value.
  Every third element in the list must be displayed in red and the remaining elements in black.
  Each of the list elements should follow the format <li style="">text_to_be_inserted</li>
  
  Question 3:
  Create a class method in Java to use provided Validate class method to validate the given name and if it's true, reverse it to all lowercase and return, else throw illigalArgumentException. 
  This question is fairly simple as the hard part which is validate method is given.
  
