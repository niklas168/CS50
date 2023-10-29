def convert(b: str):
    c=b.replace(":)","🙂").replace(":(","🙁")
    return c

def main():
    a=input()
    print(convert(a))

if __name__ == "__main__":
    main()