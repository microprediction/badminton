from badminton.live import live

def test_live():
    values = live()
    assert len(values)>=2
