from html_to_markdown import to_markdown

def test_italics():
    html = 'This is in <em>italics</em>. So is <em>this</em>'
    expected = 'This is in *italics*. So is *this*'
    actual = to_markdown(html)
    assert actual == expected

def test_spaces():
    html = 'This sentence has a    lot of    \ninteresting white spaces.'
    expected = 'This sentence has a lot of interesting white spaces.'
    actual = to_markdown(html)
    assert actual == expected

def test_single_paragraph():
    html = '<p>This is a paragraph.</p>'
    expected = 'This is a paragraph.'
    actual = to_markdown(html)
    assert actual == expected

def test_multiple_paragraphs():
    html = '<p>This is a paragraph.</p><p>This is another\nparagraph.</p>'
    expected = 'This is a paragraph.\n\nThis is another paragraph.\n\n'
    actual = to_markdown(html)
    assert actual == expected


    actual = to_markdown(html)
    assert actual == expected