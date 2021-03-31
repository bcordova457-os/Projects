# Author: Brandon Cordova
# Program: ModesOfOperation.py
# Purpose: This program has a key:'f007ba11ba5eba11' and 5 cipher-texts. The cipher-text and IV are then put through the modes of operation.
# This program displays the decrypted plain-text -bc

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = DES.block_size  # assigning block_size = size of des block for ecb and cbc modes
key = bytes.fromhex('f007ba11ba5eba11') #key used for des

# ciphers = a 2d array containing both the initialization vector and the ciphertext
ciphers = [
    [bytes.fromhex('191668e63c6d7c45'), bytes.fromhex('642763807A446B983C2DC98F22DE55084029561948986D1F022E038A623CB3BF5170D32EDBCD931B1345E7A20F1682D24D7155C3FF12253807CB10C380CF73BE6C227DDB5575E6DFA5FBEB8DEC816F7539DEA86B92CFD46349103D144F69F32C527FAB28CCCB8CE9')],
    [bytes.fromhex('f09d673319595818'), bytes.fromhex('69E702527C085514EAB60238E264478D52DA7D29A307714BC72194E79B88D89A404F414488E0B0425B87707CF1DE5339FB93005C2C0C36F68354422DCD856F26067C00031A6D7ADD44BFEBBE581E55E780D8578FA27FDBA8')],
    [bytes.fromhex('39db1a2d187e4e3a'), bytes.fromhex('05F35DB483266439CFB4B4C0895E21949587C6FF0C00A92970FAEF212DB82E70749A9805376FE09D446E8D1020CC358761D96E40BE29983C5EBC4CD5475018CA01A373FDCCA24552772BE286A1981B410E1631FFF9DD4785271D72C9FCA0711FDE46EF8803047B6682AC717BEE35E0EA596BA1D5E8FBBB1F55822F6F81FAC37CDCF5A2A50895B98F9BE45EEB7C9620C57A8BBB2688EF038035EFF57918423B16112A16282B51CEBFE1033CE4C835240493A0A5E1E8A4B91D93F07FD361130ACD64512C51323B4DD729CDD62227C95F98D3B89024CC4403B48F5E1096D41BFF8C439B442AFA894C5236D32098B2FC970452732206392A09457A91B705406B0142')],
    [bytes.fromhex('bb2dda8bcc8d6b63'), bytes.fromhex('B74F7AAFA1B90BFD668CA566C6BF038C1F04586CDD166C3657CE1C4D055D0B7B5E95EBE1020E11687363510F4E1C954F45ECED211F92A6974F7BD34CF564CE5FB69C167366A7535B2FE3E8252F703DDB326E712BD9A65450DA3C2DBAE2B97CEA1AA9F9AB1FB61690CA62CF4B86CE090647B3575BF237595E1EA35A917FA7FD5AF5EC0C31B578B37532EB4720E7A70A3235385A1C63527794')],
    [bytes.fromhex('746daff7ce2056cd'), bytes.fromhex('E29F0CD88555CA72FB34F1A0C7CD270FFBA564752C5A9F471C0DDBC6983120DA63EB63CD7CCBE32F65EEDF158BB31C31DC225BC0BB8D464DE55BA8E84E8D8F5D27A4C42D881D1A2640ED58B7C99A11D7255C181543C4C7EEE9440368174C6C00738FD26320E96C3A63A0C8A5907F8799DDFB9BD7944C96BC72EF8BF815CCE53615CA5B7E32CCBC9938A880C6CF1ECA2BD2C9EE69692871C18C68E6E2B3F3F7179E46C60EFD3700B2C93204CF1182FA4524ACB93E49C5AC9BA4BA7202E1E164DD743040CFDBDAB964A82CA30FEB875F77EE9433FA97F9489F9630D5CC12C6769E6249E635C78026F41F6BA0FA36C23557D130653A9D576BD3D20D74F068ECE65EFCF115AC389F19E7AB1EF3316380D44A51F6FD')]
    ]

# the following ecb_mode function takes the ciphertxt1 value and decrypts it, storing
# it in value msg_dec. Afterwards, we print the original ciphertxt1 in hex, and
# then print the string version, unpadding it.
print("")
def ecb_mode(ciphers):
    cipher = DES.new(key, DES.MODE_ECB)
    msg_dec = cipher.decrypt(ciphers[1])
    print("ECB Cipher: " + str(ciphers[1].hex()))
    print("Plaintext: " + str(unpad(msg_dec, BLOCK_SIZE).strip()))

ecb_mode(ciphers[0])

print("")

def cbc_mode(ciphers):
    cipher = DES.new(key, DES.MODE_CBC, ciphers[0])
    msg_dec = cipher.decrypt(ciphers[1])
    print("CBC Cipher: " + str(ciphers[1].hex()))
    print("Plaintext:" + str(unpad(msg_dec, BLOCK_SIZE).strip()))

cbc_mode(ciphers[2])

print("")

def cfb_mode(ciphers):
    cipher = DES.new(key, DES.MODE_CFB, iv=ciphers[0], segment_size=64)
    msg_dec = cipher.decrypt(ciphers[1])
    print("CFB Cipher: " + str(ciphers[1].hex()))
    print("Plaintext: " + str(msg_dec).strip())

cfb_mode(ciphers[4])

print("")

def ofb_mode(ciphers):
    cipher = DES.new(key, DES.MODE_OFB, ciphers[0])
    msg_dec = cipher.decrypt(ciphers[1])
    print("OFB Cipher: " + str(ciphers[1].hex()))
    print("Plaintext: " + str(msg_dec).strip())

ofb_mode(ciphers[3])

print("")

def ctr_mode(ciphers):
    cipher = DES.new(key, DES.MODE_CTR, nonce=ciphers[0][0:4])
    msg_dec = cipher.decrypt(ciphers[1])
    print(f"CTR Cipher: {str(ciphers[1].hex())}")
    print(f"Plaintext: {str(msg_dec).strip()}")

ctr_mode(ciphers[1])