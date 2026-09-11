from renewable_forecasting_benchmark.metrics import mae, rmse, smape

def test_metrics():
    assert mae([1, 2], [1, 4]) == 1.0
    assert rmse([1, 2], [1, 4]) > 1
    assert smape([0, 0], [0, 0]) == 0
