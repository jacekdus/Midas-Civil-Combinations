from typing import List

from App.CombinationTree.NodeData import NodeData
from App.Midas.MidasCombination import MidasCombination
from App.Midas.MidasLoadCase import MidasLoadCase
from App.Midas.MidasLoadCaseCollection import MidasLoadCaseCollection


class Converter:
    @staticmethod
    def comb_node_data_to_midas_combination(comb_node_data: List[List[NodeData]], name) -> List[MidasCombination]:
        print('Converting combination node data to midas combination...')
        midas_combs = []
        counter = 1
        for comb in comb_node_data:
            midas_load_case_collection = MidasLoadCaseCollection([])
            for node_data in comb:
                midas_load_case = MidasLoadCase(node_data.type, node_data.name, node_data.factor)
                midas_load_case_collection.load_cases.append(midas_load_case)
            midas_combination = MidasCombination(name + '_' + str(counter), midas_load_case_collection)
            midas_combs.append(midas_combination)
            counter += 1

        return midas_combs