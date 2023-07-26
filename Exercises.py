{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Exercise 1 - Class Inheritance"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create an Employee class that sets an employee's first name, last name, job title, salary, and email. The Employee class should have a class attribute for the raise amount set to 5% (1.05). Create a method that will apply the raise to an employee's salary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Employee():\n",
    "    raise_amount = 1.10\n",
    "    \n",
    "    def __init__(self, first, last, salary):\n",
    "        self.first = first\n",
    "        self.last = last\n",
    "        self.salary = salary\n",
    "        self.email = first + \".\" + last + \"@company.org\"\n",
    "        \n",
    "    def full_name(self):\n",
    "        return f'{self.first} {self.last}'\n",
    "    \n",
    "    def apply_raise(self):\n",
    "        self.salary = int(self.salary * self.raise_amount)\n",
    "        \n",
    "    def change_last_name(self, last):\n",
    "        self.last = last\n",
    "        self.email = self.first + \".\" + last + \"@company.org\"\n",
    "        \n",
    "    def add_health_benefits(self, provider):\n",
    "        self.insurance = provider\n",
    "    \n",
    "    \n",
    "emp_1 = Employee('Leo', 'Messi', 50000)\n",
    "emp_2 = Employee('Sergio', 'Aguero', 100000)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create two more classes that inherit from the Employee class. One for Sales and one for Development. Both of these classes will have the same attributes as the Employee.<br>\n",
    "- For the Sales employees, add a phone number attribute on instantiation using the super method. \n",
    "- Create a method on the Sales class that will Send a Follow Up Email. It should take in a customer name and \"send\" aka print a formatted email \"Dear *customer*, Thank you for your interest in our product. Please let me know if you have any questions. My email is *email* or my phone number is *phone number*. Thanks, *full name*\"\n",
    "- Create a method on the Development class called code that will print out \"*full name* is writing code\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Sales(Employee):\n",
    "    def __init__(self, first, last, salary, job_title, phone):\n",
    "        super().__init__(first, last, salary, job_title)\n",
    "        self.phone = phone\n",
    "        \n",
    "    def follow_up(self, customer):\n",
    "        return f\"Dear (customer), thank you for youinterest in our product. Please let me know if you have any questions. My email is {self.email} or my phone number is {self.phone}. Thanks\"\n",
    "    \n",
    "class \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Create an instance of a Sales Employee with a salary of $50,000.\n",
    "- Send follow up emails to \"Mike O'Neil\" and \"Hannah Stern\"\n",
    "- Give the employee a raise and print the salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Create an instance of a Development Employee with a salary of $100,000\n",
    "- Write some code with this employee\n",
    "- Give the employee a raise and print the salary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Exercise 2 - Importing Modules"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In VS Code, create a module titled `geometry` and add two functions in there. One that will calculate the area of a circle given a radius. The second will find the hypotenuse of a right angle given the two sides. Import the module or the functions from the module and use it to find the answers to the below questions"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is the area of a circle with a radius of 7cm?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "pi.square   answer is 100 and something"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What is the hypotenuse of a right angle with sides of 3in and 4in?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "answer is 5"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
