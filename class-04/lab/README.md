# Lab: Garage Band with OOP

## Overview

Creating a Garage Band with Object Oriented Programming.

## Configuration

Use `Poetry` to create your project with name **pythonic-garage-band**

## Repository set-up

- Create a new repository named `pythonic-garage-band`.
- Use feature branches for your work.

## Feature Tasks and Requirements

Use Python classes to model a `Band` made up of different kinds of musicians.

Start with `Guitarist`,`Bassist`, and `Drummer`.

Make use of a `Musician` base class to handle common functionality which particular kinds of musicians will inherit.

### User Acceptance Tests

Unit tests will be supplied for this lab. Your job is to make them pass. Do **NOT** modify the supplied tests (except to enable for stretch goals.)


#### Band Tests

- A `Band` instance should have a `name` attribute which is a string.
- A `Band` instance should have a `members` attribute which is a list of instances that inherit from `Musician` base (or super) class.
- A `Band` instance should have a `play_solos` method that asks each member musician to play a solo, in the order they were added to band.
- A `Band` instance should have appropriate `__str__` and `__repr__` methods.
- A `Band` should have a class method `to_list` which returns a list of previously created `Band` instances

#### Musician Subclass Tests

- Each kind of `Musician` instance should have appropriate `__str__` and `__repr__` methods.
- Each kind of `Musician` instance should have a `get_instrument` method that returns string.
- Each kind of `Musician` instance should have a `play_solo` method that returns string.

#### Stretch

- See tests marked "stretch" in supplied test suite.
- Make Musician "abstract" - aka an Abstract Base Class
- Add your own tests.

## Submission Instructions

<!-- example -->
Refer to the the [Submitting Poetry Lab Submission Instructions](../../../reference/submission-instructions){:target="_blank"} for the complete lab submission process and expectations
