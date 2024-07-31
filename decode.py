import streamlit as st
from datetime import datetime
import requests
import time
import hmac
import hashlib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import uuid
import json
import io
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import base64
import os
import sys


def getPasswd(six_code):
    six_code=bytes(six_code,encoding='utf-8')
    pwd = base64.b64encode(six_code)
    salt = b'interrupt'
    sha_obj = hashlib.sha256()
    sha_obj.update(pwd + salt)
    return sha_obj.hexdigest()[:8]


def main():
    code = st.text_input("请输入转换码")
    t_code = getPasswd(code)
    if st.button("换码"):
            if len(code)==0:
                st.write("请先输入转换码")
            else:
                st.write(f"转换后的密码为\n{t_code}")


if __name__ == "__main__":
    main()