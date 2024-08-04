et’s start by the “Work” section:

We have an issue with the focus (moving from one link to another with the TAB key) in the Desktop version. With the DevTools, you can active the focus on the <a> inside .card-title and nothing happen.

To solve it, we need to update the way we are managing the hover state of .card-title:

In your keyboard/01-styles.css file, in the /* Card WORK section
Remove opacity: 0 inside .card-work .card-title
Remove .card-work:hover .card-inner
Remove .card-work:hover .card-title
