#  Question 23: Solve the Tower of Hanoi using stacks.
def tower_of_hanoi_stacks(num_disks, source, destination, auxiliary):
    """
    Solves the Tower of Hanoi puzzle using stacks to represent the pegs.

    Args:
        num_disks: The number of disks to move.
        source: The source stack (list).
        destination: The destination stack (list).
        auxiliary: The auxiliary stack (list).
    """
    if num_disks > 0:
        tower_of_hanoi_stacks(num_disks - 1, source, auxiliary, destination)

        disk = source.pop()
        destination.append(disk)
        print(f"Move disk {disk} from {get_stack_name(source)} to {get_stack_name(destination)}")

        tower_of_hanoi_stacks(num_disks - 1, auxiliary, destination, source)

def get_stack_name(stack):
    """Helper function to get the name of the stack for printing."""
    if "source_stack" in globals() and stack is source_stack:
        return "Source"
    elif "destination_stack" in globals() and stack is destination_stack:
        return "Destination"
    elif "auxiliary_stack" in globals() and stack is auxiliary_stack:
        return "Auxiliary"
    return "Unknown"

num_disks = 3
source_stack = list(range(num_disks, 0, -1))
destination_stack = []
auxiliary_stack = []

print("Initial state:")
print(f"Source: {source_stack}")
print(f"Destination: {destination_stack}")
print(f"Auxiliary: {auxiliary_stack}")
print("-" * 20)

tower_of_hanoi_stacks(num_disks, source_stack, destination_stack, auxiliary_stack)

print("-" * 20)
print("Final state:")
print(f"Source: {source_stack}")
print(f"Destination: {destination_stack}")
print(f"Auxiliary: {auxiliary_stack}")