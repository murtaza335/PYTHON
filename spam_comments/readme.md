
### 1. `spam_keywords` List

```python
spam_keywords = [
    "free",
    "click here",
    "subscribe",
    "buy now",
    "limited time offer",
    "act now",
    "call now",
    "exclusive deal",
    "winner",
    "congratulations",
    "claim your prize",
    "visit our website",
    "don't miss out",
    "order now",
    "guaranteed",
    "100% free",
    "risk-free",
    "credit card",
    "earn money",
    "make money",
    "work from home",
    "get rich",
    "instant access",
    "no cost",
    "low cost",
    "cheap",
    "discount",
    "clearance",
    "deal",
    "bargain",
    "offer",
    "urgent",
    "important",
    "alert",
    "save big",
    "save money",
    "limited supply",
    "supplies are limited",
    "while supplies last",
    "special promotion",
    "click the link",
    "visit our site",
    "win",
    "winning",
    "prize",
    "award",
    "gift",
    "bonus",
    "free trial",
    "trial offer",
    "money-back guarantee",
    "satisfaction guaranteed",
    "no obligation",
    "easy terms",
    "fast cash",
    "fast money",
    "get paid",
    "extra income",
    "residual income",
    "be your own boss",
    "work at home",
    "online biz op",
    "email marketing",
    "seo",
    "search engine optimization",
    "internet marketing",
    "social media marketing",
    "internet biz",
    "online business",
    "home business",
    "internet business",
    "clickbank",
    "forex",
    "weight loss",
    "lose weight",
    "fat loss",
    "diet",
    "nutrition",
    "supplements",
    "pills",
    "miracle cure",
    "cure",
    "pharmacy",
    "medication",
    "drugs",
    "viagra",
    "cialis",
    "levitra",
    "casino",
    "gambling",
    "betting",
    "poker",
    "slots",
    "bingo",
    "jackpot",
    "lottery",
    "sweepstakes",
    "dating",
    "singles",
    "meet singles",
    "adult",
    "xxx",
    "porn",
    "sex",
    "nude",
    "naked",
    "loan",
    "mortgage",
    "debt",
    "consolidation",
    "bankruptcy",
    "investment",
    "stocks",
    "bonds",
    "trading",
    "broker",
    "retirement",
    "pension",
    "mutual fund",
    "real estate",
    "property",
    "luxury",
    "finance",
    "financial",
    "credit score",
    "credit report",
    "free credit",
    "repair your credit",
    "credit repair",
    "credit card debt",
    "bad credit",
    "good credit",
    "zero percent",
    "low interest",
    "refinance",
    "refinancing",
    "car loan",
    "auto loan",
    "student loan",
    "payday loan",
    "cash advance",
    "apply now",
    "get approved",
    "approval",
    "approved",
    "funding",
    "grant",
    "grants",
    "scholarship",
    "scholarships",
    "money",
    "cash",
    "payday",
    "consolidate",
    "consolidation",
    "eliminate debt",
    "reduce debt",
    "debt relief",
    "save thousands",
    "personal loan",
    "business loan",
    "loan approval",
    "loan offers",
    "loan rates",
    "best rates",
    "lowest rates",
    "mortgage rates",
    "mortgage refinance",
    "home loan",
    "bad credit loan",
    "credit score"
]
```

- **Description**: This is a Python list containing strings that are commonly found in spam messages. These strings cover a wide range of topics typically used to lure recipients into clicking on links, buying products, or providing personal information. The list includes terms related to offers, promotions, financial services, adult content, pharmaceuticals, gambling, loans, and more.

### 2. `check_spam` Function

```python
def check_spam(comment):
    check = False
    for keyword in spam_keywords:
        if keyword.lower() in comment:
            check = True
            break
    if check:
        print("This is a spam comment")
    else:
        print("Not a spam comment")
```

- **Description**: 
  - **Function Definition**: `check_spam(comment)` takes a single argument `comment`, which is expected to be a string representing a user's comment or message.
  - **Initialization**: It initializes a boolean variable `check` to `False`.
  - **Keyword Checking**: It iterates through each keyword in the `spam_keywords` list.
    - **Case Insensitivity**: Converts both the keyword and the comment to lowercase using `keyword.lower()` and `comment.lower()` respectively to ensure case insensitivity.
    - **Spam Detection**: Checks if the lowercase version of any keyword is present in the lowercase version of the comment. If a match is found, it sets `check` to `True` and exits the loop.
  - **Result Printing**: After checking all keywords, it prints "This is a spam comment" if `check` is `True`, indicating that the comment contains spam-related content. Otherwise, it prints "Not a spam comment".

### 3. User Interaction

```python
comment = input("enter comment: ")
check_spam(comment.lower())
```

- **Description**:
  - **User Input**: Prompts the user to enter a comment using `input("enter comment: ")`.
  - **Function Call**: Passes the user's input (converted to lowercase for consistency) to the `check_spam` function to determine if it contains any of the spam keywords.
  - **Output**: Depending on whether any spam keywords are found in the comment, it prints either "This is a spam comment" or "Not a spam comment".

### Summary

This script effectively identifies potential spam comments by checking for the presence of known spam-related keywords. It uses a predefined list of keywords and simple string matching techniques to make its determination. However, it's important to note that this approach may not catch all forms of spam, as spammers continually evolve their tactics.
