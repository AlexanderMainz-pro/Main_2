def test_function():
    def inner_function():
        print(f"Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function()#внутренние функции локально ограничены родительской функцией. Они существуют только внутри родительской
                # функции как локальные переменные. Попробуйте вызвать и получитe ошибку