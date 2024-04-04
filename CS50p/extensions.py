def main():
    name=((input("File name: ").strip()).lower())


    if ".gif" in name:
        print("image/gif")
        return
    if ".jpg" in name:
        print("image/jpeg")
        return
    if ".jpeg" in name:
        print("image/jpeg")
        return
    if ".png" in name:
        print("image/png")
        return
    if ".pdf" in name:
        print("application/pdf")
        return
    if ".txt" in name:
        print("text/plain")
        return
    if ".zip" in name:
        print("application/zip")
        return
    else:
        print("application/octet-stream")
        return

main()