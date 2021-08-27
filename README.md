# `namedtuple` Maker

![GitHub Actions Status](https://img.shields.io/github/workflow/status/wwt/devasc-data-formats/Markdown%20Linting?logo=github "GitHub Actions Status")

## :snake: Easily Convert Python iterable objects to `namedtuple` objects

:white_check_mark: Convert an iterable object into a `namedtuple` object using a decorator function.
:white_check_mark: Provide the `namedtuple` attribute names in a `kwarg` of the decorated function, or enter attribute names at prompts.

### :computer: Installation

Install via Python pip

```bash
pip install namedtuple-maker
```

### :warning: Requirements

- Python 3.9+

### :star: Usage as a Decorator

<details><summary>**Decorator Example**</summary>

1. Create an iterable object:

    ```python
    my_favorites = (
        'pizza',
        'summer',
        'too personal'
    )
    ```

2. Import the `convert_to_namedtuple` decorator function:

    ```python
    from namedtuple_maker.namedtuple_maker import named_tuple_converter
    ```

3. Create a function that returns an iterable object, and decorate that function with the `convert_to_namedtuple` decorator function:

```python
@named_tuple_converter
def tuple_to_namedtuple(
    iterable_input=my_favorites
):

    return iterable_input
```

4. Call the `tuple_to_namedtuple` function:
    - By default, you will receive a prompt to provide an attribute name for each iterable value.
    - You may instead pass an iterable in the `attribute_names` parameter, to use as attribute names.

    ```python
    my_named_favorites = make_named_tuple(
        iterable_input=my_favorites
    )
    ```

    ```text
    Enter an attribute name for the value "pizza": food
    Enter an attribute name for the value "summer": season
    Enter an attribute name for the value "too personal": sports team
    ```

5. Display the resulting `namedtuple` object:

    ```python
    print(my_named_favorites)
    ```

6. Observe `print` function output:

    ```text
    NamedTuple(food='pizza', season='summer', sports_team='too personal')
    ```

</details>

### :computer: Usage as a Function

<details><summary>**Function Example**</summary>

1. Create an iterable object:

    ```python
    my_favorites = (
        'pizza',
        'summer',
        'too personal'
    )
    ```

2. Import the `make_named_tuple` function:

    ```python
    from namedtuple_maker.namedtuple_maker import make_named_tuple
    ```

3. Supply the `make_named_tuple` function an argument with an iterable.

    ```python
    my_namedtuple = make_named_tuple(
        iterable_input: my_favorites
    )
    ```

3. Call the `make_named_tuple` function:
    - By default, you will receive a prompt to provide an attribute name for each iterable value.
    - You may instead pass an iterable in the `attribute_names` parameter, to use as attribute names.

    ```python
        my_named_favorites = make_named_tuple(
            iterable_input=my_favorites
        )
    ```

    ```text
    Enter an attribute name for the value "pizza": food
    Enter an attribute name for the value "summer": season
    Enter an attribute name for the value "too personal": sports team
    ```

4. Display the resulting `namedtuple` object:

    ```python
    print(my_named_favorites)
    ```

5. Observe `print` function output:

    ```text
    NamedTuple(food='pizza', season='summer', sports_team='too personal')
    ```

</details>

---

## :bulb: Overview

Python `tuple` objects are great, right?  So are `list`, `set`, and many other iterable Python objects. However, accessing the values of an iterable by an arbitrary index number makes my code hard to read.  For example, the following `list` object stores data about foods I might eat in a given day:

```python
my_meals = [
    'pizza',
    'blueberry pancakes',
    'granola',
    'fruit smoothie',
    'rice and beans'
]
```

Let's say that I want to access the values in the `my_food` list within my code. I might do that with **list indexing** like this:

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

That works just fine, although it's not terribly intuitive to associate a `list` (or `tuple`) index with a certain meal of the day since this particular list doesn't have the my meals in any particular order. The list index assigned to each meal is arbitrary.

---

## :books: The Python `namedtuple` Function

The `collections` module in the Python Standard Library includes the [`namedtuple` function](https://docs.python.org/3/library/collections.html#collections.namedtuple), which allows you to, as the name implies, create tuple-like objects with values that you can reference by name.  What does that mean, practically? Well, it means that you can access values in an iterable object by an attribute name that is much more meaningful than an index number. Using attribute names makes my code look more clean and, I think, easier for someone else to look at and understand.

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

The key difference between the `list` example and the `namedtuple` example is, accessing the values in the `namedtuple` object uses named attributes, rather than arbitrary numbers. For me, it's much easier to remember that the food I ate for breakfast is available as `my_foods.breakfast`, within in a `namedtuple` object, than it is to remember arbitrary `list` index references like my-foods[3].

---

## :bamboo: The Zen of Python

### Part I

The [Zen of Python](https://www.python.org/dev/peps/pep-0020/ "Zen of Python") is a great guide for how to write clean and effective Python code. These few lines of extract from the `import this` command output reflect the spirit of accessing attribute values by _explicit_ names, rather than _arbitrary_ numbers.

```text
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Readability counts.
```

### Part II

Below is another extract of output from the `import this` command. Given that `namedtuple` objects take significantly more code to create than, for example, `tuple` objects, using `namedtuple` objects can make it difficult to comply with the Zen of Python intent.

```text
The Zen of Python, by Tim Peters

Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
```

---

## :vertical_traffic_light: Simplifying the Complex

TBD
