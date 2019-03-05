# -*- coding: utf-8 -*-
"""
Class Model bloc
"""

class ModelBloc:

    def __init__(self, name, modelName, attributs):
        self.name = name
        self.modelName = modelName
        self.attributs = attributs

    def get_name(self):
        return self.name

    def get_attributs(self):
        return self.attributs

    def write_bloc(self):
        with open('generate/'+self.modelName+'/'+self.name+'.model.ts', 'w') as modelBloc:
            modelBloc.write('export interface '+self.name+' {\n')
            for attribut in self.attributs:
                for key, value in attribut.items():
                    modelBloc.write('\t'+key+': '+value+';\n')
                #modelBloc.write('\t'+attribut[0]+':'+attribut[1])
            modelBloc.write('}')
        modelBloc.close()