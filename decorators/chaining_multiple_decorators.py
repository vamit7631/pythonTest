def upperTextString(func):
    def wrapper():
        return func().upper()
    return wrapper

def addStringText(func):
    def wrapper():
        return func() + "Thanks for updating me!!"
    return wrapper


@upperTextString
@addStringText
def textStringData():
    return "hello Amit! "

print(textStringData())