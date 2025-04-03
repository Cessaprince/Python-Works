TEST.PY FILE EXPLANATION

For any value of k, t will be reduced by 1 till it gets to tri_recursion(0)
If k = 6:
  result = 6 + tri_recursion(5)
  result = 5 + tri_recusrion(4)
  result = 4 + tri_recursion(3)
  result = 3 + tri_recusrion(2)
  result = 2 + tri_recursion(1)
  result = 1 + tri_recusrion(0)
  result = 0

Then you go back to 1 + tri_recursion(0) ==> 1 + 0 = 1 [its going to print out since there's a print(result)]
then, 2 + tri_recursion(1) ==> 2 + 1 = 3
then, 3 + tri_recursion(2) ==> 3 + 3 = 6
then, 4 + tri_recursion(3) ==> 4 + 6 = 10
then, 5 + tri_recursion(4) ==> 5 + 10 = 15
then, 6 + tri_recursion(5) ==> 6 + 15 = 21

And after every tri_recursion() where k != 0, a print is going to occur


