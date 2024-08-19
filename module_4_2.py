def test_function(*args):
    def inner_function():
        def inner_function_2():
            print(f"Я в области видимости функции test_function")

        inner_function_2()
    inner_function()
    return inner_function()

test_function()
