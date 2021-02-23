## While Loops

Repeats a set of statements as long as the condition is True.

### DRY: Don't Repeat Yourself

### Formula
```python
while (Condition):
  # Body Code

else: # Optional
  # Body Code
```

*Ex.*
```python
while(True):
  print("This statement prints forever")
```

### Rules

A loop becomes an infinate loop if condition never becomes __FALSE__

To avoid an infinate loop, make sure to use a variable and keep track of its value.

*Ex.*

```python
counter = 0

while(counter < 3):
  print("Inside Loop")
  counter += 1 # counter = counter + 1

print("Outside Loop")
```

> Inside Loop
> Inside Loop
> Inside Loop
> Outside Loop