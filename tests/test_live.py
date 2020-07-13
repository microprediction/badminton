from badminton.replay import get_fake_live_data

def test_live():
    values = get_fake_live_data()
    assert len(values)>=2
