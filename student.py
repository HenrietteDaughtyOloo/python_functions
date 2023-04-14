def year_of_birth(name,age):
    year = 2023 - age
    print(f"hello {name} you were born in {year}")

def great(*names):
    for name in names:
        print(f"Hello {name}")