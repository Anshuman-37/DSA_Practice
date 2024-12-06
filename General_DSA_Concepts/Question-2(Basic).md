### Question 2: Differentiate between Time Complexity and Space Complexity 

Time Complexity and Space Complexity are two fundamental concepts in computer science and algorithm analysis. 
They provide insights into how an algorithm performs in terms of time (execution speed) and space (memory usage) as the size of the input data grows. 
Understanding the distinction between these two complexities is crucial for designing efficient algorithms and optimizing resource usage.

#### Time Complexity:
Definition: Measures the amount of time an algorithm takes to run as a function of the length of the input.

Purpose: Helps in evaluating and comparing the speed and efficiency of algorithms.

#### Space Complexity:
Definition: Measures the amount of memory an algorithm uses in relation to the input size.

Purpose: Assesses the memory requirements and ensures that algorithms are feasible within the available memory constraints.

#### Key Differences

| **Aspect**                   | **Time Complexity**                                         | **Space Complexity**                                         |
|------------------------------|-------------------------------------------------------------|--------------------------------------------------------------|
| **Focus**                    | Execution time of an algorithm                              | Memory usage of an algorithm                                 |
| **Measurement**              | Number of basic operations or steps executed               | Amount of additional memory allocated during execution       |
| **Impact Factors**           | CPU speed, number of operations, algorithm efficiency      | Data structures used, temporary storage, recursion depth    |
| **Optimization Goals**       | Reduce the number of operations to speed up execution       | Minimize memory usage to fit within constraints              |
| **Common Metrics**           | Best-case, average-case, worst-case scenarios              | Auxiliary space vs. total space (including input)           |
| **Examples of Consideration**| Loops, recursive calls, nested iterations                   | Arrays, linked lists, hash tables, recursion stack          |
