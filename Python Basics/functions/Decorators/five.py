def outer():
    print("Outer function")
    
    def inner():
        print("Inner function")

    return inner
inner=outer()
inner()
inner()
inner()
inner()