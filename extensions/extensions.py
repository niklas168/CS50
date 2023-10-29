feil=input("File Name: ")
if feil.lower().endswith(".jpeg"):
    print("image/jpeg")
elif feil.lower().endswith(".jpg"):
    print("image/jpeg")
elif feil.lower().endswith(".gif"):
    print("image/gif")
elif feil.lower().endswith(".png"):
    print("image/png")
elif feil.lower().strip().endswith(".pdf"):
    print("application/pdf")
elif feil.lower().endswith(".txt"):
    print("text/plain")
elif feil.lower().endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")