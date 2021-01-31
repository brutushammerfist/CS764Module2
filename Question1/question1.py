def AsciiToBinary(AsciiCharacter: chr) -> str:
    """
    Returns the binary representation of a character in string form, defaulting to 8 bits in length.

    Parameters:
    AsciiCharacter (chr): Character to convert into binary.

    Returns:
    str: Binary representation of a character in string form.
    """
    BinString = str(bin(int.from_bytes(AsciiCharacter.encode(), 'big')))[2:]

    while (len(BinString) < 8):
        BinString = '0' + BinString

    return BinString

def BitComplement(BinString: str) -> str:
    """
    Returns the complement of the string of bits given to it.

    Parameters:
    BinString (str): Bits in string form, 0 and 1, to be complemented.

    Returns:
    str: The bitwise complement of BinString.
    """
    complement = ""

    for bit in BinString:
        if bit == '0':
            complement += '1'
        else:
            complement += '0'
    
    return complement

def Encrypt(ToEncrypt: chr, PreviousH: str) -> str:
    """
    """
    Key = BitComplement(PreviousH)
    LeftKey = Key[:4]
    RightKey = Key[4:]

    Text = AsciiToBinary(ToEncrypt)
    LeftText = Text[:4]
    RightText = Text[4:]

    LeftCipher = ""
    RightCipher = ""

    for index in range(0, len(LeftKey)):
        if (LeftKey[index] == RightText[index]):
            LeftCipher += '0'
        else:
            LeftCipher += '1'

    for index in range(0, len(RightKey)):
        if (RightKey[index] == LeftText[index]):
            RightCipher += '0'
        else:
            RightCipher += '1'
    
    return LeftCipher + RightCipher

def MartyasMeyerOseasHash(ToEncrypt: str, HZero: str) -> str:
    """
    """
    PreviousH = HZero

    for char in ToEncrypt:
        PreviousH = Encrypt(char, PreviousH)

    return PreviousH

def GenerateMerkleTree(Nodes: list, HZero: str):
    """
    """
    Tree = {}
    InputNodes = Nodes
    InputLabels = Nodes
    Layers = []
    LayerLabels = []
    LeftOver = ""
    LeftOverLabel= ""

    # Generate initial encryptions from 3 letter words
    PreviousH = HZero
    CurrentLayer = []

    for node in Nodes:
        CurrentLayer.append(MartyasMeyerOseasHash(node, PreviousH))

    Layers.append(CurrentLayer)
    LayerLabels.append(Nodes)
    InputNodes = CurrentLayer
    InputLabels = Nodes

    # While we haven't generated a root node...
    while len(Layers[-1]) > 1:
        PreviousH = HZero
        CurrentLayer = []
        CurrentLabels = []

        # If odd number of nodes, save layover 1 to allow for 2 nodes per parent node
        if len(InputNodes) % 2 == 1:
            LeftOver = InputNodes[-1]
            del InputNodes[-1]
            LeftOverLabel = InputLabels[-1]
            del InputLabels[-1]

        # Calculate Hash for parent nodes...
        idx = 0
        while idx < len(InputNodes):
            NewNode = InputNodes[idx] + InputNodes[idx + 1]
            CurrentLabels.append(InputLabels[idx] + InputLabels[idx + 1])
            CurrentLayer.append(MartyasMeyerOseasHash(NewNode, PreviousH))
            idx += 2

        # append as new layer
        Layers.append(CurrentLayer)
        LayerLabels.append(CurrentLabels)
        InputNodes = CurrentLayer
        InputLabels = CurrentLabels

        # If there is leftover, move to next layer
        if (LeftOver != ""):
            InputNodes.append(LeftOver)
            LeftOver = ""
            InputLabels.append(LeftOverLabel)


    # Root node generated, print tree layers and labels
    LayerLabels.reverse()
    Layers.reverse()
    print(LayerLabels)
    print(Layers)

if __name__ == "__main__":
    HZero = AsciiToBinary('X')

    with open("input.txt", "r") as inputFile:
        ToHash = [line.rstrip() for line in inputFile]

    GenerateMerkleTree(ToHash, HZero)