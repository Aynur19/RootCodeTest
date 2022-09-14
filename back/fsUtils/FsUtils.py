import os
import json

path = 'C:/aynur19/dev/RootCode/back/files'

def getFileAttributes(filename: str, filter: str):
    data = {
        'ext': f'.{filename.split(".")[-1]}',
        'previousName': filename
    }

    attributes = data['previousName'][:len(data['previousName'])-len(data['ext'])].split('_')
    count = len(attributes)

    attr1 = attributes[0]
    attr2 = attributes[1] if count >= 2 else None
    attr3 = ''.join(attributes[2:]) if count >= 3 else None

    if attr3 is not None and not attr3.lower().__contains__(filter.lower()):
        data['newName'] = f'{attr3}_{attr1}_{attr2}{data["ext"]}'
        data['newAttributes'] = [attr3, attr1, attr2]
    else:
        data['newName'] = None
        data['newAttributes'] = [attr1, attr2, attr3]

    data['previousAttributes'] = [attr1, attr2, attr3]

    return data


def renameFiles(directory: str, ext: str, attrFilter: str):
    files = [f for f in os.listdir(directory) if f.endswith(ext)]
    data = []

    for f in files:
        data.append((getFileAttributes(f, attrFilter)))
        if data[-1]['newName'] is not None:
            os.rename(os.path.join(path, f), os.path.join(path, data[-1]['newName']))

    with open(os.path.join(directory, "_filesPdf.json"), "w") as f:
        json.dump(data, f, indent = 4)


def resetFiles(directory: str, ext: str):
    files = [f for f in os.listdir(directory) if f.endswith(ext)]
    fileNames = ['Abc_Def_Ghi.pdf',
                 'Bcd_Efg_Hij.pdf',
                 'Cde_Fgh_Ijk.pdf',
                 'Def_Ghi_Jkl.pdf',
                 'Efg_Hij_Klm.pdf',
                 'Fgh_Ijk_Lmn.pdf',
                 'Ghi_Jkl_Mno.pdf',
                 'Hij_Klm_Nop.pdf',
                 'Ijk_Lmn_Opq.pdf',
                 'Jkl_Mno_Pqr.pdf']

    for i in range(len(fileNames)):
        os.rename(os.path.join(directory, files[i]), os.path.join(path, fileNames[i]))


def main():
    # resetFiles(path, '.pdf')
    renameFiles(path, '.pdf', 'J')


if __name__ == "__main__":
    main()
