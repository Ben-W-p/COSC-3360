def greetingFunction(name: str, greeting: str) -> None:
    print(f"{greeting} {name}")

name = input("Enter your name: ").strip()
greeting = input("Enter a greeting (e.g., Hello): ").strip()

greet = lambda n, g: print(f"{g} {n}")
greet(name, greeting)
