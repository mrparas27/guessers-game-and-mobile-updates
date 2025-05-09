class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.phone_numbers = []  # To store phone numbers associated with names


class PhoneDirectory:
    def __init__(self):
        self.root = TreeNode()

    def add_contact(self, name, phone_number):   # aman
        node = self.root
        for char in name.lower():  # Insert name into the Trie in lowercase
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.phone_numbers.append(phone_number)  # Store phone number for this contact

    def search_contacts(self, query):
        node = self.root
        for char in query.lower():  # Traverse the Trie using the query
            if char not in node.children:
                return []  # If query is not found
            node = node.children[char]
        
        # Collect all contacts under this node
        results = []
        self._collect_all_contacts(node, query, results)
        return results

    def _collect_all_contacts(self, node, prefix, results):
        if node.is_end_of_word:
            for phone_number in node.phone_numbers:
                results.append((prefix, phone_number))
        for char, child_node in node.children.items():
            self._collect_all_contacts(child_node, prefix + char, results)

    def display_all_contacts(self):
        print("\nAll Contacts:")
        results = []
        self._collect_all_contacts(self.root, "", results)
        if results:
            for name, phone in results:
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")
        print()


# Main Program
if __name__ == "__main__":
    directory = PhoneDirectory()

    while True:
        print("\nPhone Directory Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone_number = input("Enter phone number: ").strip()
            directory.add_contact(name, phone_number)
            print(f"Contact '{name}' added successfully.")

        elif choice == "2":
            query = input("Enter characters to search: ").strip()
            results = directory.search_contacts(query)
            if results:
                print("\nSearch Results:")
                for name, phone in results:
                    print(f"{name}: {phone}")
            else:
                print("No contacts found with the given characters.")

        elif choice == "3":
            directory.display_all_contacts()

        elif choice == "4":
            print("Exiting phone directory. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

