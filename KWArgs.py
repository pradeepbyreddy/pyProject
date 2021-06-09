def cheeseshop(kind, **kwargs):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    #for arg in args:
    #    print(arg)
    print("-" * 40)
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

cheeseshop("leonade", name="pradeep", name2='byreddy')