# Advanced API Project

Advanced Query Features
This API offers robust query options for the Book model, enabling precise and flexible data retrieval.

Filtering
Filter books based on specific attributes using these query parameters:

title: Find books by their title (e.g., ?title=My Book).
author: Locate books by the author's ID (e.g., ?author=1).
publication_year: Search for books by their publication year (e.g., ?publication_year=2023).
Searching
Use the search parameter to look for books by title or author. Example:

Search for books containing the keyword 'Django': ?search=Django.
Sorting
Sort the results using these fields:

title: Sort alphabetically by title (e.g., ?ordering=title).
publication_year: Sort by the year of publication (e.g., ?ordering=publication_year).
Combining Parameters
Combine multiple query parameters for more refined searches:

Example: Retrieve books published in 2023 and sort them alphabetically by title: ?publication_year=2023&ordering=title.