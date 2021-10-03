# Lab: Automation

## Overview

A colleague has abruptly left the team to pursue a career as a novelist.

This colleague's last days (and weeks) on the job were a mixed bag in terms of productivity.

Looking through the documents left behind there is some important contact info in the form of email addresses and phone numbers.

Unfortunately it's mixed in with a bunch of useless notes.

Your job is to find the needles in the haystack.

## Feature Tasks and Requirements

- Given a document `potential-contacts`, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats.
  - (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
  - phone numbers with missing area code should presume 206
  - phone numbers should be stored in xxx-yyy-zzzz format.
- Once emails and phone numbers are found they should be stored in two separate documents.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.

phone_numbers.txt

```text
123-456-7890
206-678-9012
234-567-8901
```

emails.txt

```text
ana@foo.bar
bill_x@foo.bar
chris.schmidt@bar.baz
```

## Stretch Goals

- It turns out some of the contacts are already in our system.
  - Compare your collected data against `existing-contacts.txt` and only include info NOT already in system.
- Handle phone numbers with extensions. E.g. (123) 456-789x012

### User Acceptance Tests

The 'phone_numbers.txt' and 'emails.txt' files will be verified by an automated system. So make sure to match the naming/formatting requirements exactly.

## Configuration

- Find `potential-contacts.txt` and `existing-contacts.txt` in folder `assets` for today's class in course repo.

Use `poetry` to create `automation` project.

```console
> $ poetry new automation
```

Use the folder created by Poetry as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
