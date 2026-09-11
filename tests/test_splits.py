from renewable_forecasting_benchmark.splits import chronological_split
def test_split():
    a,b,c=chronological_split(list(range(10)))
    assert a[-1] < b[0] < c[0]
