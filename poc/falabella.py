#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Example module to perform relative imports"""


def fif_hi(name="Falabella Inversiones Financieras"):
    """ test function """
    flag = True if name != "Falabella Inversiones Financieras"  else False
    print("Hola %s" % name)
    return flag
