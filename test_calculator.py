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
