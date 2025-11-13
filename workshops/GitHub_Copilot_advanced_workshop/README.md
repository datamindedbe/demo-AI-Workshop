# Gilded Rose Refactoring Kata - GitHub Copilot Advanced Workshop

This workshop uses the Gilded Rose Refactoring Kata to practice advanced GitHub Copilot features including test generation, refactoring, and code documentation.

## About the Gilded Rose Kata

The Gilded Rose is a classic refactoring kata originally created by Terry Hughes. It simulates a real-world legacy code scenario where you need to add new features to existing code that's difficult to understand and modify.

You can find out more about this exercise in Emily Bache's YouTube video [Why Developers LOVE The Gilded Rose Kata](https://youtu.be/Mt4XpGxigT4).

## Workshop Setup

This project uses [UV](https://docs.astral.sh/uv/) for Python package management. UV is a fast Python package installer and resolver written in Rust.

### Prerequisites

- Python 3.11+
- UV package manager ([installation instructions](https://docs.astral.sh/uv/getting-started/installation/))
- GitHub Copilot enabled in VS Code

### Quick Start

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **You're ready to go!** The workshop will guide you through writing tests and refactoring code using GitHub Copilot.

## The Gilded Rose Requirements

Hi and welcome to team Gilded Rose! As you know, we are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods. Unfortunately, our goods are constantly degrading in `Quality` as they approach their sell by date.

We have a system in place that updates our inventory for us. Your task is to add new features to our system so that we can begin selling new categories of items.

### Current System Rules

- All `items` have a `SellIn` value which denotes the number of days we have to sell the items
- All `items` have a `Quality` value which denotes how valuable the item is
- At the end of each day our system lowers both values for every item

### Special Rules

- Once the sell by date has passed, `Quality` degrades twice as fast
- The `Quality` of an item is never negative
- **"Aged Brie"** actually increases in `Quality` the older it gets
- The `Quality` of an item is never more than `50`
- **"Sulfuras"**, being a legendary item, never has to be sold or decreases in `Quality`
- **"Backstage passes"**, like aged brie, increases in `Quality` as its `SellIn` value approaches:
  - `Quality` increases by `2` when there are `10` days or less
  - `Quality` increases by `3` when there are `5` days or less
  - `Quality` drops to `0` after the concert

### New Feature Request

We have recently signed a supplier of conjured items. This requires an update to our system:

- **"Conjured"** items degrade in `Quality` twice as fast as normal items

### Constraints

- Do not alter the `Item` class or `Items` property (the goblin in the corner who owns that code will insta-rage!)
- An item can never have its `Quality` increase above `50`, except **"Sulfuras"** which is legendary and has `Quality` of `80` that never alters

## Workshop Exercises

### Exercise 1: Understanding the Code with Copilot
- Use Copilot Chat to explain what the `update_quality()` method does
- Ask Copilot to generate documentation for the existing code
- Use inline suggestions to add comments explaining complex logic

### Exercise 2: Writing Tests with Copilot
- Use Copilot to help you write comprehensive test cases
- Start from scratch or build on the basic test structure
- Test all item types: Normal, Aged Brie, Sulfuras, Backstage passes
- Create tests for edge cases (negative quality, quality > 50, expired items)
- Explore approval testing with `texttest_fixture.py`

### Exercise 3: Refactoring with Copilot
- Use Copilot to help break down the complex `update_quality()` method
- Extract methods for different item types
- Consider using design patterns (Strategy, Factory, etc.)
- Run your tests frequently to ensure nothing breaks

### Exercise 4: Implementing the Conjured Items Feature
- Add support for "Conjured" items using Copilot suggestions
- Write tests first (TDD approach)
- Implement the feature so Conjured items degrade twice as fast
- Refactor to make the solution clean and maintainable

## Useful Commands

### Running Python Code
```bash
uv run python <filename>.py
```

### Running Tests (once you've written them!)
```bash
uv run pytest                          # Run all tests
uv run pytest tests/ -v                # Run with verbose output
uv run pytest tests/test_file.py       # Run specific test file
```

### Simulate the Shop
```bash
uv run python texttest_fixture.py 10  # Simulate 10 days
```

### Code Coverage (advanced)
```bash
uv run coverage run -m pytest          # Run tests with coverage
uv run coverage report                 # View coverage report
```

## Tips for Using GitHub Copilot

1. **Use clear comments** - Write what you want before the code and let Copilot suggest implementations
2. **Leverage Copilot Chat** - Ask questions about the codebase, request explanations, or get refactoring suggestions
3. **Test-Driven Development** - Write test descriptions first and let Copilot suggest test implementations
4. **Iterative refinement** - Accept suggestions and refine them, don't expect perfect code on first try
5. **Use `/tests` command** - In Copilot Chat to generate comprehensive test suites
6. **Use `/fix` command** - To get suggestions for fixing issues
7. **Use `/doc` command** - To generate documentation for code

## Resources

- [Emily Bache's GildedRose Kata Repository](https://github.com/emilybache/GildedRose-Refactoring-Kata)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [UV Documentation](https://docs.astral.sh/uv/)
- [Pytest Documentation](https://docs.pytest.org/)

## History of the Exercise

This Kata was originally created by Terry Hughes. It is already on GitHub [here](https://github.com/NotMyself/GildedRose). The kata has been translated into many programming languages by Emily Bache and the community. This version has been adapted for a GitHub Copilot workshop.

## Contributing

This workshop is part of the demo-AI-Workshop repository. Contributions and improvements are welcome!

---

_Original kata support via [Emily Bache's Patreon](https://www.patreon.com/EmilyBache)_
