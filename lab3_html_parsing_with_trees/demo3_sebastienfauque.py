import pytest
from sebastienfauqueLab3 import ListCollector

def test_list_collector_example():
    html_content = """ <html>
    <head>
    <title>W3C Mission Summary</title>
    </head>
    <body>
    <h1>W3C Mission</h1>
    <p>
    The W3C mission is to lead the World Wide Web to its full potential<br>
    by developing protocols and guidelines that ensure the long-term growth of the Web.
    </p>
    <h2>Principles</h2>
    <ul>
    <li>Web for All</li>
    <li>Web on Everything</li>
    </ul>
    See the complete <a href="http://www.w3.org/Consortium/mission.html">W3C Mission document</a>.
    </body>
    </html>
    """
    # Initialize and feed the HTML to the  parser
    collector = ListCollector()
    collector.feed(html_content)

    # Expected output
    expected_lists = [
        ['Web for All', 'Web on Everything']
    ]

    # Get the lists from the parser and assert equality
    assert collector.getLists() == expected_lists

def test_list_collector():
    html_content = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
      <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <title>ListCollector parser test file</title>
      </head>
      <body>
        <h1>Test file for ListCollector parser</h1>
        This HTML document contains an unordered and an ordered list. First
        the unordered one:<br>
        <h3>Unordered list</h3>
        <ul>
          <li>An item</li>
          <li>Another</li>
          <li>And another one</li>
        </ul>
        Next is the ordered one.<br>
        <h3>Ordered List</h3>
        <ol>
          <li>Item one</li>
          <li>Item two</li>
          <li>Item three</li>
          <li>Item four</li>
        </ol>
        End of input.<br>
      </body>
    </html>
    """

    # Initialize and feed the HTML to the  parser
    collector = ListCollector()
    collector.feed(html_content)

    # Expected output
    expected_lists = [
        ['An item', 'Another', 'And another one'],
        ['Item one', 'Item two', 'Item three', 'Item four']
    ]

    # Get the lists from the parser and assert equality
    assert collector.getLists() == expected_lists
