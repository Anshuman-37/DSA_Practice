## Question 10: Difference between Pass By Value and Pass By Reference

### Pass By Value

#### Definition

When arguments are passed by value, a copy of the actual data is made and passed to the function. This means that the
function operates on the copy, and any modifications made within the function do not affect the original data outside
the function.

#### Characteristics

* Isolation: Changes inside the function don't impact the original variable.
* Safety: Prevents unintended side-effects since the original data remains unchanged.
* Memory Usage: Can consume more memory if large data structures are copied.

#### Example

```c++
#include <iostream>
using namespace std;

void increment(int num) {
    num = num + 1;
    cout << "Inside function: " << num << endl; // Outputs 11
}

int main() {
    int a = 10;
    increment(a);
    cout << "Outside function: " << a << endl; // Outputs 10
    return 0;
}
```

### Pass By Reference

#### Definition

When arguments are passed by reference, a reference (or address) to the actual data is passed to the function. This
allows the function to operate directly on the original data, meaning that any changes made within the function do
affect the original variable.

#### Characteristics

* Direct Access: Functions can modify the original data.
* Efficiency: Avoids copying large data structures, saving memory and processing time.
* Risk: Increases the risk of unintended side-effects since the original data can be altered.

#### Example

```c++
#include <iostream>
using namespace std;

void increment(int &num) { // Note the & indicating pass by reference
    num = num + 1;
    cout << "Inside function: " << num << endl; // Outputs 11
}

int main() {
    int a = 10;
    increment(a);
    cout << "Outside function: " << a << endl; // Outputs 11
    return 0;
}
```

### Language Specific

* _C++_: Supports both pass by value and pass by reference using the & symbol.
* _Java_:  Uses pass by value for all variable types. However, object references are passed by value, meaning the
  reference itself is copied, but both the original and the copy refer to the same object. This can sometimes behave
  similarly to pass by reference.
* _Python_: Uses a mechanism called "pass by object reference" or "pass by assignment." Variables hold references to
  objects, and while you can't rebind the reference itself within the function, mutable objects can be modified.

### Python vs. Pass by Value and Pass by Reference

While Python's argument passing isn't strictly pass by value or pass by reference, its behavior can mimic both based on
the mutability of objects:

* For Immutable Objects: Similar to pass by value because functions cannot alter the original object.
* For Mutable Objects: Similar to pass by reference because functions can modify the original object.

However, it's crucial to understand that Python always passes the reference by value, meaning the function receives a
copy of the reference to the object, not the actual object or a copy of it.

```python
# Immutable Object Example
a --> [10]
# Function receives a copy of the reference:
num --> [10]
num += 1 # creates a new object:
num --> [11]
#a remains --> [10]

# Mutable Object Example
lst --> [1, 2, 3]
# Function receives a copy of the reference:
my_list --> [1, 2, 3]
my_list.append(4) # modifies the same object:
lst --> [1, 2, 3, 4]
my_list --> [1, 2, 3, 4]
```