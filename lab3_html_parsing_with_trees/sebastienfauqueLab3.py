from html.parser import HTMLParser

class ListCollector(HTMLParser):
    """Subclass of the HTMLParser class that collects list data from HTML.

    Overwrites default methods handle_starttag, handle_endtag,
    and handle_data."""
    def __init__(self):
        super().__init__()
        self.lists = []  # Store all the lists.
        self.current_list = None  # Store the current list being parsed.
        self.collecting_li = False  # Record if we're inside an <li> tag.

    def handle_starttag(self, tag: str, attrs: list) -> None:
        """
        Handle the start of an HTML tag.

        If the tag is 'ul' or 'ol', a new list is started.
        If the tag is 'li' and a list is being collected, data collection begins.

        Params:
            tag (str): The name of the tag.
            attrs (list): A list of (name, value) pairs containing the attributes found
                          inside the tag’s <> brackets.
        """
        if tag in ('ul', 'ol'):
            # Start a new current list
            self.current_list = []
        elif tag == 'li' and self.current_list is not None:
            # Need to collect the data in this <li> tag.
            self.collecting_li = True

    def handle_endtag(self, tag) -> None:
        """
        Handle the end of an HTML tag.

        If the tag is 'ul' or 'ol', the current list is finished and stored.
        If the tag is 'li', data collection for the current item ends.

        Params:
            tag (str): The name of the tag.
        """
        if tag in ('ul', 'ol'):
            # Finished collecting the current list
            if self.current_list is not None:
                self.lists.append(self.current_list)
                self.current_list = None
        elif tag == 'li':
            # Finished collecting the current <li> item
            self.collecting_li = False

    def handle_data(self, data: str) -> None:
        """
        Handle the textual content within an HTML tag.

        If currently collecting an 'li' item, the text data is added to the
        current list, with whitespace stripped.

        Params:
            data (str): The textual content within the tag.
        """
        if self.collecting_li and self.current_list is not None:
            # Add the text data to the current list and remove whitespace.
            self.current_list.append(data.strip())

    def getLists(self) -> list[list[str]]:
        """
        Get the lists collected from the HTML document.

        Returns:
            list[list[str]]: A list containing all the lists collected from the
                             HTML document. Each list contains the text data
                             of the items.
        """
        return self.lists
