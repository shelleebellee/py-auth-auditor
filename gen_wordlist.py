import itertools

def create_list():
    base_words = ["CompanyX", "2026", "Admin", "Secure"]
    special_chars = ["!", "@", "#"]
    output_file = "custom_passwords.txt"
    
    with open(output_file, 'w') as f:
        for word in base_words:
            for char in special_chars:
                for year in ["2025", "2026"]:
                    f.write(f"{word}{char}{year}\n")
                    f.write(f"{char}{word}{year}\n")
                    f.write(f"{word}{year}{char}\n")
    print(f"[+] Successfully generated {output_file}")

if __name__ == "__main__":
    create_list()

