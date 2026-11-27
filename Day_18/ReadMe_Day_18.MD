Today's learning objectives
By the end of Day 18, you should understand:
1. Fixture dependencies.
2. Setup and teardown.
3. The yield keyword in fixtures.
4. Fixture scope in practice.
5. Automatic fixtures using autouse=True.
6. How to organize reusable test data.

![img.png](img.png)

Use return when you only need to provide data.

Use yield when you need cleanup after the test.

**Lesson 1:**  **Fixture dependencies.**

The Idea: Sometimes, you need to build one LEGO piece before you can attach another piece on top of it. In pytest, one fixture can ask for another fixture to do its job first!


**Lesson 2 & 3:** **Setup, Teardown & Why yield?**

The Idea: Imagine setting up a tea party (Setup), playing the tea party (The Test), and washing the cups afterward (Teardown).
• return is like handing someone a cup of tea and walking away forever—you never come back to clean up.
• yield is like saying, "Here is the cup. I will pause right here while you drink it. When you are done, I will wake up and clean the cup!"


**Lesson 4: Autouse & Fixture Scope (How Often Do We Reset?)**

• autouse=True: Normally, a test only gets a fixture if it asks for it by name. autouse=True is like a ninja—it runs automatically for every test without being asked!
• Fixture Scope: This controls how often the setup runs:
	• scope="function" (Default): Runs fresh for every single test (like washing your plate after every meal).
	• scope="module": Runs only once for the entire Python file (like setting up a dining table once for the whole day).
