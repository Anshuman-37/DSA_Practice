# Question 18: Create a phone directory using a hash map for lookups.
class PhoneDirectory:
    def __init__(self):
        self.directory = {}  # Using a dictionary (hash map)

    def add_entry(self, name: str, number: str) -> None:
        self.directory[name] = number

    def lookup_number(self, name: str) -> str | None:
        return self.directory.get(name)

    def delete_entry(self, name: str) -> None:
        if name in self.directory:
            del self.directory[name]

    def update_number(self, name: str, new_number: str) -> None:
        if name in self.directory:
            self.directory[name] = new_number
        else:
            print(f"Error: {name} not found in the directory.")

    def get_all_entries(self) -> dict[str, str]:
        return self.directory

# Example Usage:
phone_dir = PhoneDirectory()
phone_dir.add_entry("Alice", "123-456-7890")
phone_dir.add_entry("Bob", "987-654-3210")

print(phone_dir.lookup_number("Alice"))
print(phone_dir.lookup_number("Charlie"))

phone_dir.delete_entry("Bob")
print(phone_dir.get_all_entries())

phone_dir.update_number("Alice", "111-222-3333")
print(phone_dir.lookup_number("Alice"))