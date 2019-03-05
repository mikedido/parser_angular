# -*- coding: utf-8 -*-
"""
Class Model
"""

class Model:

    def __init__(self, name, attributs, blocs):
        self.name = name
        self.attributs = attributs
        self.blocs = blocs

    def write_model(self):
        with open('generate/'+self.name+'/'+self.name+'.model.ts', 'w') as model:
            for bloc in self.blocs:
                model.write('import {'+bloc.get_name()+'} from \'./'+bloc.get_name()+'.model\';\n')
            model.write('\n')
            model.write('export interface '+self.name+' {\n')
            for bloc in self.blocs:
                model.write('\t'+bloc.get_name()+': '+bloc.get_name()+';\n')
            model.write('}')
        model.close()

    def write_bloc(self):
        for bloc in self.blocs:
            bloc.write_bloc()