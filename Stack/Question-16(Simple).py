# Question 16: Check if two stacks can produce the same pop sequence.
def can_produce_same_pop_sequence(stack1, stack2, target_sequence):
    def can_produce(stack, sequence):
        temp_stack = []
        seq_index = 0
        stack_index = 0

        while seq_index < len(sequence):
            if temp_stack and temp_stack[-1] == sequence[seq_index]:
                temp_stack.pop()
                seq_index += 1
            elif stack_index < len(stack):
                temp_stack.append(stack[stack_index])
                stack_index += 1
            else:
                return False
        return True

    return can_produce(stack1, target_sequence) and can_produce(stack2, target_sequence)


stack1_a = [1, 2, 3]
stack2_a = [3, 2, 1]
target_a = [3, 2, 1]
print(
    f"Stacks {stack1_a} and {stack2_a} can produce {target_a}: {can_produce_same_pop_sequence(stack1_a, stack2_a, target_a)}")

stack1_b = [1, 2, 3]
stack2_b = [4, 5, 6]
target_b = [1, 2, 3]
print(
    f"Stacks {stack1_b} and {stack2_b} can produce {target_b}: {can_produce_same_pop_sequence(stack1_b, stack2_b, target_b)}")

stack1_c = [1, 2]
stack2_c = [3, 4]
target_c = [1, 3, 2, 4]
print(
    f"Stacks {stack1_c} and {stack2_c} can produce {target_c}: {can_produce_same_pop_sequence(stack1_c, stack2_c, target_c)}")

stack1_d = [1, 2]
stack2_d = [3, 4]
target_d = [1, 4, 2, 3]
print(
    f"Stacks {stack1_d} and {stack2_d} can produce {target_d}: {can_produce_same_pop_sequence(stack1_d, stack2_d, target_d)}")

stack1_e = [1, 2]
stack2_e = [3, 4]
target_e = [1, 4, 3, 2]
print(
    f"Stacks {stack1_e} and {stack2_e} can produce {target_e}: {can_produce_same_pop_sequence(stack1_e, stack2_e, target_e)}")
