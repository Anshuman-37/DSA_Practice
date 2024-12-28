# Question 19: Given (person,boss) pairs, build a hierarchy (org chart) using a hash map.

from collections import defaultdict

def build_hierarchy(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Builds an organizational hierarchy from (person, boss) pairs using a hash map.

    Args:
        pairs: A list of tuples, where each tuple is (person, boss).

    Returns:
        A dictionary representing the hierarchy, where keys are bosses and
        values are lists of their direct reports.
    """
    hierarchy = defaultdict(list)
    for person, boss in pairs:
        hierarchy[boss].append(person)
    return hierarchy

def find_root(pairs: list[tuple[str, str]]) -> str | None:
    """
    Finds the root of the hierarchy (the ultimate boss).
    """
    employees = set(person for person, _ in pairs)
    bosses = set(boss for _, boss in pairs)
    potential_roots = bosses - employees
    if len(potential_roots) == 1:
        return potential_roots.pop()
    else:
        return None

def print_hierarchy(hierarchy: dict[str, list[str]], boss: str, indent=0):
    """
    Prints the hierarchy in a tree-like structure.
    """
    print("  " * indent + boss)
    for employee in sorted(hierarchy.get(boss, [])):
        print_hierarchy(hierarchy, employee, indent + 1)

employee_boss_pairs = [
    ("Alice", "Bob"),
    ("Charlie", "Alice"),
    ("David", "Bob"),
    ("Eve", "Charlie"),
    ("Frank", "David"),
    ("Grace", "Root")
]

hierarchy = build_hierarchy(employee_boss_pairs)
print("Hierarchy Hash Map:", hierarchy)

root = find_root(employee_boss_pairs)
if root:
    print("\nOrganizational Chart:")
    print_hierarchy(hierarchy, root)
else:
    print("\nCould not determine a single root for the hierarchy.")