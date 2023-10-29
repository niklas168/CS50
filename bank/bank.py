greet=input("Greeting: ")
cash=0
if "hello" not in greet.lower():
        if greet[0].lower()=="h":
            cash=20
        else:
            cash=100

print(f"${cash}")

