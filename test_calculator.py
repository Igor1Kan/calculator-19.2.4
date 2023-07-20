# test_calculator.py
import tkinter as tk
from math import sqrt
from tkinter import ttk

import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    root = tk.Tk()
    calc = Calculator(root)
    yield calc
    root.destroy()


def test_button_click(calculator):
    calculator.button_click(1)
    assert calculator.number_entry.get() == "1"


def test_button_clear(calculator):
    calculator.number_entry.insert(0, "123")
    calculator.clear()
    assert calculator.number_entry.get() == ""


def test_button_add(calculator):
    calculator.number_entry.insert(0, "5")
    calculator.add()
    assert calculator.math == "addition"
    assert calculator.f_num == 5
    assert calculator.number_entry.get() == ""


def test_button_equal(calculator):
    calculator.number_entry.insert(0, "5")
    calculator.add()
    calculator.number_entry.insert(0, "7")
    calculator.equal()
    assert calculator.number_entry.get() == "12"


def test_button_subtract(calculator):
    calculator.number_entry.insert(0, "10")
    calculator.subtract()
    assert calculator.math == "subtraction"
    assert calculator.f_num == 10
    assert calculator.number_entry.get() == ""


def test_button_multiply(calculator):
    calculator.number_entry.insert(0, "6")
    calculator.multiply()
    assert calculator.math == "multiplication"
    assert calculator.f_num == 6
    assert calculator.number_entry.get() == ""


def test_button_divide(calculator):
    calculator.number_entry.insert(0, "20")
    calculator.divide()
    assert calculator.math == "division"
    assert calculator.f_num == 20
    assert calculator.number_entry.get() == ""

def test_button_floor_div(calculator):
    calculator.number_entry.insert(0, "15")
    calculator.floor_div()
    assert calculator.math == "floor_div"
    assert calculator.f_num == 15
    assert calculator.number_entry.get() == ""
