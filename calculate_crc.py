from sys import byteorder


def recalculate_crcs(target_modfile, coin_palette_crcs:list):
    """
    Patches the two CRC values used by the N64 boot chip to verify the integrity
    of the ROM (0x10 and 0x14). Paper Mario uses the CIC-NUS-6103 boot chip, so
    we must use the corresponding algorithm to calculate the new CRCs.
    Reproducing the correct unsigned integer arithmetic is tricky and leads to
    this ugly, nigh-unreadable code. But it works.
    This function's workings were provided by clover's StarRod crc patching
    functionality.
    """
    if coin_palette_crcs is None:
        with open(target_modfile, "r+b") as file:
            t1 = 0xA3886759 # 6103 only
            t2 = 0xA3886759 # 6103 only
            t3 = 0xA3886759 # 6103 only
            t4 = 0xA3886759 # 6103 only
            t5 = 0xA3886759 # 6103 only
            t6 = 0xA3886759 # 6103 only

            file.seek(0x1000)
            for i in range(0x100000//4):
                d = int.from_bytes(file.read(4), "big") & 0xFFFFFFFF
                if ((t6 + d) & 0xFFFFFFFF) < (t6 & 0xFFFFFFFF):
                    t4 += 1
                t6 += d
                t3 ^= d

                r = (d << (d & 0x1F)) | (d >> (32 - (d & 0x1F))) & 0xFFFFFFFF

                t5 += r
                if (t2 & 0xFFFFFFFF) > (d & 0xFFFFFFFF):
                    t2 ^= r
                else:
                    t2 ^= (t6 ^ d)

                t1 += t5 ^ d

            crc1 = ((t6 ^ t4) + t3) & 0xFFFFFFFF
            crc2 = ((t5 ^ t2) + t1) & 0xFFFFFFFF

            file.seek(0x10)
            file.write(crc1.to_bytes(4, byteorder="big"))
            file.write(crc2.to_bytes(4, byteorder="big"))

    else:
        print("writing provided crc")
        with open(target_modfile, "r+b") as file:
            file.seek(0x10)
            for crc in coin_palette_crcs:
                file.write(crc.to_bytes(4, byteorder="big"))
