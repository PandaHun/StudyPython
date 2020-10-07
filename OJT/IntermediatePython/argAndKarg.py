def test_var_args(f_arg, *args):
    """*args used send non-keyworded variables, unspecified number of argument """
    print('the first argument is', f_arg)
    for arg in args:
        print('another arg is', arg)


test_var_args('yahoo', 'yaha', 'yoho')


def greet_me(**kargs):
    """**kargs allow pass keyworded vairable length of argument"""
    for key, value in kargs.items():
        print('{0} = {1}'.format(key, value))


greet_me(name='yaho')


def test_args_kwargs(arg1, arg2, arg3):
    print('arg1', arg1)
    print('arg2', arg2)
    print('arg3', arg3)

args = ("two", 3, 5)
test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)