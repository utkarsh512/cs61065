"""
CS61065 - Theory and Applications of Blockchain
Assignment - 1
Part - A

Author - Utkarsh Patel (18EC35034)
"""

import hashlib


class MerkleNode:
    """Node in a Merkle tree

    It has three data members:
    - data:  content of the node
    - left:  left child of the node
    - right: right child of the node
    """

    def __init__(self, data=None, left=None, right=None):
        """Constuct current node

        :param data: content of the node
        :type data: str
        :param left: left child of the node, defaults to None
        :type left: MerkleNode, optional
        :param right: right child of the node, defaults to None
        :type right: MerkleNode, optional
        """
        self.data  = data
        self.left  = left
        self.right = right
        
        if self.data is None:
            self.set_data()


    @property
    def hash(self):
        """`md5` hash for the current node

        :return: md5 hash
        :rtype: str
        """
        return hashlib.md5(self.data.encode('utf-8')).hexdigest()

    
    def set_data(self):
        """Set data field using left and right childs
        """
        self.data = self.left.hash + self.right.hash



class MerkleTree:
    """Merkle tree for a block
    """

    def __init__(self, transactions):
        """Constructs a MerkleTree object

        :param transactions: transactions for the block
        :type transactions: list[str]
        """ 
        self.transactions = transactions
        self._root = None

    
    @property
    def root(self):
        """Root of the Merkle tree

        :rtype: MerkleNode
        """
        if self._root is None:
            self._root = self.build_tree()
        return self._root.hash

    
    def build_tree(self):
        """Builds the Merkle tree

        :return: Root of the Merkle tree
        :rtype: MerkleNode
        """
        return self.build_tree_rec([MerkleNode(data=data) for data in self.transactions])


    def build_tree_rec(self, nodes):
        """Builds the Merkle tree recursively

        :param nodes: MerkleNode objects in the current level
        :type nodes: list[MerkleNode]
        """
        if len(nodes) == 1:
            return nodes[0]

        if len(nodes) & 1:
            # Odd number of nodes in the current level.
            # Duplicate the last node.
            nodes.append(nodes[-1])

        new_nodes = list()
        for i in range(0, len(nodes), 2):
            new_nodes.append(MerkleNode(left=nodes[i], right=nodes[i + 1]))
        return self.build_tree_rec(new_nodes)


def is_valid(transactions, root_hash):
    """Tests whether the merkle tree root provided is correct for given 
    transactions

    :param transactions: transactions in the block
    :type transactions: list[str]
    :param root_hash: Merkle root
    :type root_hash: str
    """
    tree = MerkleTree(transactions)
    return tree.root == root_hash


if __name__ == '__main__':
    n_blocks = int(input())
    for _ in range(n_blocks):
        n_txs = int(input())
        txs = list()
        for i in range(n_txs):
            txs.append(input())
        root = input()
        if is_valid(txs, root):
            print('Valid')
        else:
            print('Invalid')
