# README

This project contains a collection of exercies and learnings based around the topics of;

- Python Test Runners (unittest)
- Unit Testing
- Integration Testing
- End to End Testing

## Python Test Runners (unittest)
We use the python module `unittest` to write our Unit Tests. The `unittest` module gives us the base class we need to be able to use `assertion methods` to write our tests. In this example `unittest.TestCase` iis the base class in question which has to be imported at the start of each test file.

```
import unittest

class TestFancyText(unittest.TestCase):
```

## Unit Testing

### /unittesting_1
How to write Positive and Negitive Unit Tests.

#### Assertion Methods
```
self.assertEqual()
```

Asserting that a function failes in a known way (negitive test cases)

```
self.assertRaises
```

### /unittesting_2

In this project we will look at `parameterized` testing. This allows us to write our Tests in a slightly more orderly way - grouping tests by relivance. Most importantly it allows us to write much fewer test functions.

We need to use a python module / library called [parameterized](https://pypi.org/project/parameterized/) to achieve this.