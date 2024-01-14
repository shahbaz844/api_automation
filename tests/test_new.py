import pytest
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def test_new():
    print('newwwww testttttt')
    print(f'envvv varssss {os.getenv("USER")}')
