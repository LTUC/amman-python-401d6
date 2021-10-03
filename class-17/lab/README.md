# Lab: Web Scraping

## Overview

It's wonderful when someone has gone to the effort to expose their site's data through an API.

But not everyone can (or wants to) do that.

No problem. Let's code up a web scraper that can automate the process of manually using the site.

## Feature Tasks and Requirements

- Scrape a Wikipedia page and record which passages need citations.
  - E.g. [History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico){:target="_blank"} has a few "citations needed".
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
  - E.g. Citation needed for "lorem spam and impsum eggs"
  - Consider the "relevant passage" to be the parent element that contains the passage, often a paragraph element.

## Implementation Notes

- Count function must be named **get_citations_needed_count**
  - get_citations_needed takes in a url and returns an integer
- Report function must be named **get_citations_needed_report**
  - get_citations_needed_report takes in a url and returns a string
  - the string should be formatted with each citation needed on own line, in order found.
- Module must be named **scraper.py**

## Stretch Goals

- Organize the needed citations by section (i.e. the parent heading tag)
  - Name additional function **get_citations_needed_by_section**
- Automatically do a citation scan for any links from the main section of wikipedia page.


### User Acceptance Tests

- verify that correct count of citations needed is calculated
- verify that preceding passage

## Configuration

>$ poetry new web-scraper

Use the folder created by Poetry as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
