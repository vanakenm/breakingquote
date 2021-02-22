from breakingquote.lib import quote

def test_quote():
  result = quote()
  assert "-" in result.split()
