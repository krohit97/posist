from Crypto.Cipher import AES

class node:
	def __init__(self, timestamp, data, nodeNumber, nodeId, referenceNodeId, childReferenceNodeId, genesisReferenceNodeId, HashValue):
		self.timestamp = timestamp
		self.data = data
		self.nodeNumber = nodeNumber
		self.nodeId = nodeId
		self.referenceNodeId = referenceNodeId
		self.childReferenceNodeId = childReferenceNodeId
		self.genesisReferenceNodeId = genesisReferenceNodeId
		self.HashValue = HashValue

# Limit to 2 child only
class list:
	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None
		self.parent = None 

	def insert(self, data):
		if self.left == None:
			if data < self.data:
				self.left = list(data)
		elif self.right == None:
			if data < self.data:
				self.right = list(data)
		else:
			insert(self.left)
			insert(self.right)

	def encrypt(self):
		obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
		ciphertext = obj.encrypt(self.data)
		
	def decrypt(ciphertext):
		obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
		return obj2.decrypt(ciphertext)


def createGenesis():
	

def createChild()

def encryptNode()

def decryptNode()

def verifyOwner()

def editNode()

def transferOwnership()

def longestChainGenesis()

def longestChain()

def merge()

# Main 
while true:
	print("1. Create genesis node.")
	print("2. Create child node.")
	print("3. Encrypt node data.")
	print("4. Decrypt node data")
	print("5. Verify Owner.")
	print("6. Edit node.")
	print("7. Transfer Ownership.")
	print("8. Longest chain of genesis node.")
	print("9. Longest chain of any node.")
	print("10. Merge nodes.")
	print("11. Exit")

	choice = raw_input("Enter your choice: ")

	if choice == 11:
		break
	elif choice == 1:
		createGenesis()
	elif choice == 2:
		createChild()
	elif choice == 3:
		encryptNode()
	elif choice == 4:
		decryptNode()
	elif choice == 5:
		verifyOwner()
	elif choice == 6:
		editNode()
	elif choice == 7:
		transferOwnership()
	elif choice == 8:
		longestChainGenesis()
	elif choice == 9:
		longestChain()
	elif choice == 10:
		merge()






