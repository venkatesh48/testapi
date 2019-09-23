# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:23:38 2019

@author: venkatesh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:25:19 2019

@author: venkatesh
"""

from flask import Flask,request, jsonify
from flask_cors import CORS,cross_origin
import os

app = Flask(__name__)

@app.route('/python/kuberflow/api', methods=['POST'])
@cross_origin(origins = '*')
def apicall():
    
    output_response=[  
                           {  
                              "errorDetails":{  
                                 "error_description":"",
                                 "error_type":""
                              },
                              "output":[  
                                 {  
                                    "content_type":"",
                                    "encoding_type":"",
                                    "output":""
                                 }
                              ],
                              "responseTypeCode":"1",
                              "result":""
                           }
                        ]
    try: 
        test_json = request.get_json()
        extract_params=test_json['parameters']
        
        output_response={'output':'hi '+extract_params }
        
        
    except Exception as e:
        
        output_response={'ouput':'problem in api'}

    return jsonify(output_response)

@app.route('/python/kubeflow/test', methods=['GET'])
@cross_origin(origins = '*')
def post_voice():

	return "health"

if __name__ == '__main__':
   app.run(host='127.0.0.1',port=5000,debug = True)