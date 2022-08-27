"""
CS61065 - Theory and Applications of Blockchain
Assignment - 1
Part - B

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


class Block:
    """Block for a given set of transactions

    It has four data members:
    - version:       the block version
    - previous_hash: previous block header hash
    - merkle_tree:   Merkle tree for the transactions
    - hash:          current block hash
    """

    def __init__(self, transactions, previous_hash='', version='02000000'):
        self.merkle_tree = MerkleTree(transactions)
        self.previous_hash = previous_hash
        self.version = version
    

    @property
    def hash(self):
        """`md5` hash for the current block

        :return: md5 hash
        :rtype: str
        """
        header = self.version + self.previous_hash + self.merkle_tree.root
        return hashlib.md5(header.encode('utf-8')).hexdigest()


if __name__ == '__main__':
    n_blocks = int(input())
    blocks = list()
    previous_hashes = list()

    # Add genesis block
    blocks.append(Block(transactions=['coinbase']))
    
    for _ in range(n_blocks):
        n_txs = int(input())
        txs = list()
        for i in range(n_txs):
            txs.append(input())
        previous_hashes.append(input())
        blocks.append(Block(txs, blocks[-1].hash))

    for i in range(1, len(blocks)):
        if blocks[i].previous_hash == previous_hashes[i - 1]:
            print("Valid")
        else:
            print("Invalid")