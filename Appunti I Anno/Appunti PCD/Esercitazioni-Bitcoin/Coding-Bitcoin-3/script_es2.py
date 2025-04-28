# Parsing the following locking script: 6e879169a87ca887. Using the descriptions
# of the opcodes, determine what an unlocking script should contain to produce
# a script that evaluates to True.

from io import BytesIO
import helpers


class Script:
    def __init__(self, cmds):
        self.cmds = cmds

    def __str__(self):
        return " ".join([str(x) for x in self.cmds])

    @classmethod
    def parse(cls, bs):
        r = BytesIO(bs)
        script_len = len(bs)  # lunghezza dello script
        count = 0
        cmds = []
        while count < script_len:
            first = int.from_bytes(r.read(1), "little")
            count += 1
            if 1 <= first <= 75:
                # Push data of length first
                cmds.append(r.read(first).hex())
                count += first
            elif first == 76:
                data_len = int.from_bytes(r.read(1), "little")
                cmds.append(r.read(data_len).hex())
                count += data_len + 1
            elif first == 77:
                data_len = int.from_bytes(r.read(2), "little")
                cmds.append(r.read(data_len).hex())
                count += data_len + 2
            elif first == 78:
                data_len = int.from_bytes(r.read(4), "little")
                cmds.append(r.read(data_len).hex())
                count += data_len + 4
            else:  # first è OP_CODE
                cmds.append(helpers.OPCODES[first])
        return cls(cmds)


if __name__ == "__main__":
    locking_script_hex = "6e879169a87ca887"
    locking_script = bytes.fromhex(locking_script_hex)
    parsed_script = Script.parse(locking_script)

    print("Parsed Locking Script:", parsed_script)
    
    # gli opcodes sono: op_2dup op_equal op_not op_verify op_sha256 op_swap op_sha256 op_equal
    
    # Che unlocking script ci serve?
    # Supponiamo che nell'unlocking script vengano messi due elementi: chiamiamoli X e Y.
    # Passo dopo passo:
    # Stack iniziale: X Y
    # OP_2DUP: X Y X Y
    # OP_EQUAL: compara X e Y
    #     Se uguali, restituisce 1
    #     Se diversi, restituisce 0
    # OP_NOT: inverte
    #     Se erano uguali: 0
    #     Se erano diversi: 1
    # OP_VERIFY: serve che il valore sia 1 → quindi X e Y devono essere DIVERSI.
    # Conclusione 1: X ≠ Y
    # Proseguendo:
    # OP_SHA256: fa SHA256 di X → stack: hash(X) Y
    # OP_SWAP: stack: Y hash(X)
    # OP_SHA256: fa SHA256 di Y → stack: hash(Y) hash(X)
    # OP_EQUAL: confronta hash(Y) e hash(X), deve dare 1.
    # Conclusione 2: hash(X) = hash(Y)
    # Riassunto:
    # X ≠ Y
    # SHA256(X) = SHA256(Y)
    unlocking_script = "X Y"

    print("Unlocking Script:", unlocking_script)
