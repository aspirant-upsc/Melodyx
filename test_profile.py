from handlers.profile import set_fancy, get_fancy_for_user

def test_set_and_get():
    set_fancy(999999, 'testuser', '*', '*', '*test*')
    val = get_fancy_for_user(999999)
    assert val == '*test*'
