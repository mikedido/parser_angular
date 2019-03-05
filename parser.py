# -*- coding: utf-8 -*-
import yaml
import re
import os
import shutil
# import package
from package.Model import Model
from package.ModelBloc import ModelBloc


"""
Programme de génération de model en angular.
"""
blocRegex = r"^bloc[0-9]*$"
blocList = []
i=0

#reading models
for model in os.listdir('models'):
    with open('models/'+model, 'r') as stream:
        data_loaded = yaml.load(stream)
        #delete the directiry if exist
        if os.path.exists('generate/'+data_loaded['model']['name']) == True:
            shutil.rmtree('generate/'+data_loaded['model']['name'])
        #create the directory model
        os.mkdir('generate/'+data_loaded['model']['name'])

    for section in data_loaded['model']:
        #gestion des blocs 
        if re.search(blocRegex, section) is not None:
            #set a new model bloc
            blocList.append(ModelBloc(data_loaded['model'][section]['name'], data_loaded['model']['name'], data_loaded['model'][section]['attributs']))
            i+=1

    #set the global model
    modelGlobal = Model(data_loaded['model']['name'], data_loaded['model']['attributs'], blocList)
    modelGlobal.write_model()
    modelGlobal.write_bloc()