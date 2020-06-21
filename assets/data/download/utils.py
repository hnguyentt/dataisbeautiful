"""
Module for data downloading
"""
import requests
import pandas as pd


def html2tsv(url):
    """
    Read html, get the second table
    :param url:
    :param out:
    :return:
    """
    res = requests.get(url)
    data = pd.read_html(res.text)

    return data[1]
