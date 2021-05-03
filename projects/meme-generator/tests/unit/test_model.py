from QuoteEngine.model import QuoteModel


def test_quote_str():
    q = QuoteModel("Veni, vidi, vici.", "Julius Caesar")
    assert str(q) == '"Veni, vidi, vici." - Julius Caesar'
