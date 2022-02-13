# Import dependency
# from flask import Flask
# Create a new Flask app instance
# app = Flask(__name__)
# Create Flask Routes
# @app.route('/')
# def hello_world():
#    return 'Hello world'


# SET-UP THE DATABASE
# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import dependencies needed for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import dependencies needed for Flask
from flask import Flask, jsonify

# Set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()

# Reflect the database
Base.prepare(engine, reflect=True)

# Create a variable for each of the classes so they can be referenced later
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# SET-UP FLASK
app = Flask(__name__)

# CREATE THE WELCOME ROUTE
@app.route("/")

# Add the routing information for each of the other routes
# Create a function welcome() with a return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Create Precipitation route
@app.route("/api/v1.0/precipitation")

# Create Precipitation() function
def precipitation():
    # Calculate date one year ago from most recent date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    # Create a dictionary with date as key and ppct as value; jsonify the dictionary
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create Stations route
@app.route("/api/v1.0/stations")

# Create stations() function
def stations():
    # Create query that allows us to get stations in database
    results = session.query(Station.station).all()
    # Unravel results into 1-dimensional array  and convert results to a list() and jsonify list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create temperature observations route
@app.route("/api/v1.0/tobs")

# Create function called temp_monthly()
def temp_monthly():
    # Calculate date 1 yr ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query primary station for all temp obs in previous year; filter active station/previous year
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    # Unravel results in 1-dim array and convert to list
    temps = list(np.ravel(results))
    # jsonifiy list
    return jsonify(temps=temps)

# Create two separate routes for start and end dates for temperature
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats()
# Add start and end parameters to the function and set both to None
def stats(start = None, end = None):
    # Create query to select min, avg, max from database and set to variable "sel"
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # Use if_not to determine start and end date; query database, unravel results into 1-dim
    # array and convert to a list; jsonify results
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
    # Output is Null,Null,Null because we did not specify start and end date.  Add dates to the 
    # web browser: 2017-06-01/2017-06-30; output is min, avg, and max temps. For these dates it
    # is 71, 77.219, 83