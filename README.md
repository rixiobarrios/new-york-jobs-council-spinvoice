![download-2](https://github.com/rixiobarrios/new-york-jobs-council-spinvoice/assets/55994508/40c41c0d-3667-4033-a348-dafd9bb9cb7b)

## Task 1: Fix a critical bug

### Task instructions
Alright - let's find the bug in the Spinvoice system. Begin by downloading the invoice class.

To assist you in your search, we’ve provided a list of expectations for the system. It must fulfill the following requirements:

- An invoice tracks the name, address, and email of both its sender and recipient.
- An invoice tracks the date it was created, as well as items to charge for.
- An item may be added to an existing invoice.
- Each item has an associated name, price, and percent tax.
- The total price of an invoice is the sum of all its constituent items.
- A percent discount may be applied to the entire invoice.
- A discount must be applied before tax is determined.
- An invoice must calculate its total price based on all contained items.
 
Once you’ve had a moment to familiarize yourself with the code, start rooting around for the bug. # new-york-jobs-council-spinvoice

## Task 2: Implement a feature

### Task instructions

The organizations TechSoft deals with need a way to attach comments to invoices to help communicate the rationale for various charges. Your task is to implement this functionality in the existing system. Using the code you’ve been working on over the course of this program, create new methods within the invoice class to handle adding and viewing comments. How you choose to implement the new feature is up to you, but your solution should satisfy the following requirements:

- An invoice may contain zero or more comments.
- Comments may be added to an existing invoice.
- Invoices must expose a method that returns a string representation of all their comments.

The above are the only requirements you need to worry about. For example, there is no need to remove comments from an invoice. Pay special attention to code cleanliness, and try to implement your fix without changing unrelated code. And, of course, check to make sure your solution actually works. 

Feel free to use your own code or the example answer from Task 1.
