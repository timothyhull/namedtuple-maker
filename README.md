# `namedtuple` Maker

![GitHub Actions Status](https://img.shields.io/github/workflow/status/wwt/devasc-data-formats/Markdown%20Linting?logo=github "GitHub Actions Status")

## Overview

`tuple` objects are great, right?  So are `list` objects, `set` objects, and many other iterable Python objets. I find that accessing values stored in some iterable Python objects can make my code look a bit ugly and be tough to understand, when I access iterable object values by index.

For example, the following `list` object stores data about foods I might eat in a given day:

```python
my_meals = [
    'pizza',
    'blueberry pancakes',
    'granola',
    'fruit smoothie',
    'rice and beans'
]
```

Let's say that I want to access the values in the `my_food` list within my code. I might do that like this:

```python
print('My Meals')
print('--------')
print(f'Breakfast: {my_meals[1]}\n'
      f'Snack: {my_meals[3]}\n'
      f'Lunch: {my_meals[4]}')
```

The result from this code would be:

```text
My Meals
--------
Breakfast: blueberry pancakes
Snack: fruit smoothie
Lunch: rice and beans
```

That works just fine, although it's not terribly intuitive to associate a `list` (or `tuple`) index with a certain meal of the day since this particular list doesn't have the my meals in any particular order.

---

## The Python `namedtuple` Function

The `collections` module in the Python Standard Library includes the [`namedtuple` function](https://docs.python.org/3/library/collections.html#collections.namedtuple), which allows you to, as the name implies, create tuple-like objects with values that you can reference by name.  What does that mean, practically?  Well, it means that you can access values in an iterable object by an attribute name that is more meaningful than an index number. Using attribute names makes my code look more clean and, I think, easier for someone else to look at and understand.

For example, I'll recreate the `my_meals` data using a `namedtuple` object:

1. First, import the `namedtuple` function from the `collections` module:

    ```python
    from collections import namedtuple
    ```

2. Next, create a new object type using the `namedtuple` function.
    - Think of a `namedtuple` object like a `class` object without any methods, only named attributes.
    - The `field_names` parameter defines the attribute names for the new object.

    ```python
    Meals = namedtuple(
        typename='Meals',
        field_names=[
            'breakfast',
            'snack',
            'lunch',
            'dinner',
            'dessert'
        ]
    )
    ```

3. Now, create an instance of the `Meals` object and assign the individual foods to the named attributes (specified by the `field_names` parameter.):

    ```python
    my_meals = Meals(
        breakfast='blueberry pancakes',
        snack='fruit smoothie',
        lunch='rice and beans',
        dinner='pizza',
        dessert='granola'
    )
    ```

When I want to access or display data from the `my_meals` `namedtuple` object, my code will look something like this:

```python
print('My Meals')
print('--------')
print(f'Breakfast: {my_meals.breakfast}\n'
      f'Snack: {my_meals.snack}\n'
      f'Lunch: {my_meals.lunch}')
```

The result from this code looks exactly like it did in the first example:

```text
My Meals
--------
Breakfast: blueberry pancakes
Snack: fruit smoothie
Lunch: rice and beans
```

The difference is, to access information about the snack I ate, I didn't have to use the arbitrary index reference `my_meals[3]`.  Instead, I used a much more elegant attribute name as a reference, `my_meals.snack`.

---

## The Zen of Python (extract)

```text
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Readability counts.
```

---

## Simplifying the Complex

The syntax to create `namedtuple` objects can be somewhat cumbersome, when compared to creating a `tuple` or `list`, for example.
 