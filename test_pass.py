# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_errorRaised(self):
        self.assertRaises(pwd.getNext("zzzzz"))



    def test_hasSeries1(self):
        self.assertEqual(pwd.hasSeries("abcd"), True)

    def test_hasSeries2(self):
        self.assertEqual(pwd.hasSeries("abcz"), True)

    def test_hasSeries3(self):
        self.assertEqual(pwd.hasSeries("zabc"), True)

    def test_hasSeries4(self):
        self.assertEqual(pwd.hasSeries("cbak"), False)

    def test_hasSeries5(self):
        self.assertEqual(pwd.hasSeries("azef"), False)


    def test_hasNoBadChar1(self):
        self.assertEqual(pwd.hasNoBadChar("aiol"), False)

    def test_hasNoBadChar2(self):
        self.assertEqual(pwd.hasNoBadChar("abcl"), False)

    def test_hasNoBadChar3(self):
        self.assertEqual(pwd.hasNoBadChar("abco"), False)

    def test_hasNoBadChar4(self):
        self.assertEqual(pwd.hasNoBadChar("abci"), False)

    def test_hasNoBadChar5(self):
        self.assertEqual(pwd.hasNoBadChar("azef"), True)


    def test_hasTwoPair1(self):
        self.assertEqual(pwd.hasTwoPair("aazee"), True)

    def test_hasTwoPair2(self):
        self.assertEqual(pwd.hasTwoPair("aaeez"), True)

    def test_hasTwoPair3(self):
        self.assertEqual(pwd.hasTwoPair("aaeee"), True)

    def test_hasTwoPair4(self):
        self.assertEqual(pwd.hasTwoPair("aaaze"), False)

    def test_hasTwoPair5(self):
        self.assertEqual(pwd.hasTwoPair("aazed"), False)



# Permet d'exécuter les tests si ce fichier est exécuté
#unittest.main()