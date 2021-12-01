from typing import List

from treelib import Tree

from App.CombinationTree.LoadCombination import LoadCombination
from App.CombinationTree.NodeData import NodeData


def get_class_name(obj):
    return obj.__class__.__name__


class CombinationTree:
    def __init__(self, load_combination: LoadCombination):
        print('Preparing Combination Tree...', flush=True)
        self.tree = Tree()
        self.name = load_combination.name
        self.load_combination = load_combination
        self.root = self.create_root(load_combination.name)
        self.create_tree()
        print('Combination Tree created', flush=True)

    def create_root(self, name):
        return self.tree.create_node(name, data=NodeData(name))

    def create_tree(self):
        self._create_new_tree_lvl(self.load_combination, self.root)

    def get_comb_count(self):
        return len(self.tree.leaves())

    def get_expected_comb_count(self):
        # TODO: this method has to find envelopes in nested load cases
        count = 1
        for lc_f in self.load_combination.load_cases:
            if lc_f[0].envelop:
                length = len(lc_f[0].midas_load_cases)
                count *= length

        return count

    def get_combination_data(self):
        return self._replace_combination_ids_with_node_data(self._get_combination_ids())

    def log_basic_info(self):
        print('##### COMBINATION TREE LOG #####')
        print('Created: {} combinations'.format(str(self.get_comb_count())))
        # print('Expected: {} combinations '.format(self.get_expected_comb_count()))

    def _get_combination_ids(self):
        return self._get_combination_ids_without_root(self._get_combination_ids_with_root())

    def _get_combination_ids_with_root(self):
        return self.tree.paths_to_leaves()

    @staticmethod
    def _get_combination_ids_without_root(comb_ids):
        for comb in comb_ids:
            del comb[0]

        return comb_ids

    def _replace_combination_ids_with_node_data(self, comb_ids) -> List[List[NodeData]]:
        combs = []
        for ids in comb_ids:
            comb = []
            for id in ids:
                node = self.get_node(id)
                comb.append(node.data)
            combs.append(comb)

        return combs

    def get_node(self, nid):
        return self.tree.get_node(nid)

    def log_tree_structure(self):
        print('Combination-Tree Structure:')
        self.tree.show(data_property='value')

    def _create_node(self, lc_f, parent):
        return self.tree.create_node(lc_f[0].name, parent=parent, data=NodeData(lc_f[0].name, lc_f[1], lc_f[0].type))

    def _create_new_tree_lvl(self, lc, parent):
        if lc.envelop:
            for lc_f in lc.load_cases:
                curr_node = self._create_node(lc_f, parent)

                if get_class_name(lc_f[0]) == 'LoadCombination':
                    self._create_new_tree_lvl(lc_f[0], curr_node)
        else:
            for lc_f in lc.load_cases:
                parent_or_his_leaves = self.tree.leaves(parent.identifier)
                for leaf in parent_or_his_leaves:
                    curr_node = self._create_node(lc_f, leaf)

                    if get_class_name(lc_f[0]) == 'LoadCombination':
                        self._create_new_tree_lvl(lc_f[0], curr_node)
