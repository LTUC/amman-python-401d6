# Lab: Intro to Django

## Overview

The first words you see on the Django website are

> Django makes it easier to build better Web apps more quickly and with less code.

The next quote you'll see is

> The web framework for perfectionists with deadlines.

In this class we'll build out a small, but functional, multi page web site using Django.

We'll get a feel for the "Django Way" and see the dramatic performance gains you can get with a mature, robust framework.

## Feature Tasks and Requirements

- Create web site in Django with 2 pages
  - home page
  - about page
  - create views/urls/templates as needed for home and about pages
  - use ancestor template to contain navigation elements
  - Should be built the "Django way" aka match the structure of in-class demo

## Implementation Notes

- **Typical Steps to Start Django Project**
  - create project
  - define app
  - add app to project
  - add views
  - add urlpatterns
  - add templates
  - add tests

## User Acceptance Tests

- Use Django's built in testing tools
  - Test that `home` and `about` url status codes
  - Test `home` and `about` url template use, including ancestor template.

## Configuration

- create a Github repo named `django-snacks`
- create folder `django_snacks`
- create django project named `snacks_project`
- create django app named `snacks`

Use `poetry` to initialize project folder.


Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.


## Stretch Goals

- create additional apps in project
- pass additional info along to views and render it
- extend additional blocks in templates
