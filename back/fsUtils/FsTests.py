import unittest
from fsUtils import FsUtils

class FsUtilsTests(unittest.TestCase):
    def testGetFileAttributes(self):
        data = FsUtils.getFileAttributes('Abc_Def_Ghi.pdf..pdf', 'J')
        assert data['previousName'] == 'Abc_Def_Ghi.pdf..pdf'
        assert data['previousAttributes'] == ['Abc', 'Def', 'Ghi.']
        assert data['newName'] == 'Ghi._Abc_Def.pdf'
        assert data['newAttributes'] == ['Ghi.', 'Abc', 'Def']

        data = FsUtils.getFileAttributes('Bcd_Efg_Hi.j.pdf', 'J')
        assert data['previousName'] == 'Bcd_Efg_Hi.j.pdf'
        assert data['previousAttributes'] == ['Bcd', 'Efg', 'Hi.j']
        assert data['ext'] == '.pdf'
        assert data['newName'] == None
        assert data['newAttributes'] == ['Bcd', 'Efg', 'Hi.j']

        data = FsUtils.getFileAttributes('Cde_Fgh_I.jk.pdf', 'J')
        assert data['previousName'] == 'Cde_Fgh_I.jk.pdf'
        assert data['previousAttributes'] == ['Cde', 'Fgh', 'I.jk']
        assert data['ext'] == '.pdf'
        assert data['newName'] == None
        assert data['newAttributes'] == ['Cde', 'Fgh', 'I.jk']

        data = FsUtils.getFileAttributes('Def_Ghi_.Jkl.pdf', 'J')
        assert data['previousName'] == 'Def_Ghi_.Jkl.pdf'
        assert data['previousAttributes'] == ['Def', 'Ghi', '.Jkl']
        assert data['ext'] == '.pdf'
        assert data['newName'] == None
        assert data['newAttributes'] == ['Def', 'Ghi', '.Jkl']

        data = FsUtils.getFileAttributes('Efg_Hij._Klm.pdf', 'J')
        assert data['previousName'] == 'Efg_Hij._Klm.pdf'
        assert data['previousAttributes'] == ['Efg', 'Hij.', 'Klm']
        assert data['ext'] == '.pdf'
        assert data['newName'] == 'Klm_Efg_Hij..pdf'
        assert data['newAttributes'] == ['Klm', 'Efg', 'Hij.']

        data = FsUtils.getFileAttributes('Fgh_Ij.k_Lmn.pdf', 'J')
        assert data['previousName'] == 'Fgh_Ij.k_Lmn.pdf'
        assert data['previousAttributes'] == ['Fgh', 'Ij.k', 'Lmn']
        assert data['ext'] == '.pdf'
        assert data['newName'] == 'Lmn_Fgh_Ij.k.pdf'
        assert data['newAttributes'] == ['Lmn', 'Fgh', 'Ij.k']

        data = FsUtils.getFileAttributes('Ghi_J.kl_Mno.pdf', 'J')
        assert data['previousName'] == 'Ghi_J.kl_Mno.pdf'
        assert data['previousAttributes'] == ['Ghi', 'J.kl', 'Mno']
        assert data['ext'] == '.pdf'
        assert data['newName'] == 'Mno_Ghi_J.kl.pdf'
        assert data['newAttributes'] == ['Mno', 'Ghi', 'J.kl']

        data = FsUtils.getFileAttributes('Hij_.Klm_Nop.pdf', 'J')
        assert data['previousName'] == 'Hij_.Klm_Nop.pdf'
        assert data['previousAttributes'] == ['Hij', '.Klm', 'Nop']
        assert data['ext'] == '.pdf'
        assert data['newName'] == 'Nop_Hij_.Klm.pdf'
        assert data['newAttributes'] == ['Nop', 'Hij', '.Klm']

        data = FsUtils.getFileAttributes('Ijk._Lmn_Opq.pdf', 'J')
        assert data['previousName'] == 'Ijk._Lmn_Opq.pdf'
        assert data['previousAttributes'] == ['Ijk.', 'Lmn', 'Opq']
        assert data['ext'] == '.pdf'
        assert data['newName'] == 'Opq_Ijk._Lmn.pdf'
        assert data['newAttributes'] == ['Opq', 'Ijk.', 'Lmn']

        data = FsUtils.getFileAttributes('Jk.l_Mno_Pqr.pdf', 'J')
        assert data['previousName'] == 'Jk.l_Mno_Pqr.pdf'
        assert data['previousAttributes'] == ['Jk.l', 'Mno', 'Pqr']
        assert data['ext'] == '.pdf'
        assert data['newName'] == 'Pqr_Jk.l_Mno.pdf'
        assert data['newAttributes'] == ['Pqr', 'Jk.l', 'Mno']
