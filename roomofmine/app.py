import os

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import session
from werkzeug.security import check_password_hash, generate_password_hash

# configure application
app = Flask(__name__)