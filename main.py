import basic
while True:
    text = input('basic > s')
    result, error = basic.run('<std>', text)

    if error:
        print(error.as_string())
    else:
        print(result)