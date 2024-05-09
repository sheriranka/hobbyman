from flask import Blueprint, request, jsonify, render_template, current_app, url_for, redirect, Flask, make_response
from .database import db, Stats
import json
import os
import uuid
from sqlalchemy import text
import pandas as pd

stats = Blueprint('stats', __name__, url_prefix='/stats')


# Add time to database
@stats.route('/add_time', methods=['POST'])
def receive_gps_data():
    data = request.json
    time = data['time']
    id = data['label']
    
    
    new_row = Stats(
        time_spent=time,
        activity=id,
    )

    db.session.add(new_row)
    db.session.commit()

    return jsonify({"message": "Info logged."}), 201


@stats.route('/get_all', methods=['GET'])
def get_all_data():
    
    #query = text("SELECT * FROM stats DESC LIMIT 1")

    #row = db.engine.execute(query).fetchone()

    row = Stats.query.all()

    df = pd.DataFrame(columns=['time_spent','activity'])

    if row:

        for col in row:
            data = [col.time_spent, col.activity]
            df.loc[len(df.index)] = data

        csv_df = df.to_csv(index=False)

        resp = make_response(csv_df)

        cd = 'attachment; filename=all_stats.csv'
        resp.headers['Content-Disposition'] = cd 
        resp.mimetype='text/csv'

        return resp
      
        #return jsonify(data_return), 200
    else:
        return jsonify({"message": "No data :("}), 404