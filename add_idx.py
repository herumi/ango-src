# -*- coding:cp932 -*-
import re, sys, codecs

# re._MAXCACHE = 200

wordTbl = {
	u"Cramer-Shoup�Í�":u"Cramer-Shoup���񂲂�",
	u"ElGamal�Í�":u"ElGamal���񂲂�",
	u"RSA�Í�":u"RSA���񂲂�",
	u"RSA-OAEP":u"RSA-OAEP",
	u"��w��":u"��������",
	u"Weierstrass�̕�����":u"Weierstrass�̂ق��Ă�����",
	u"�y�[�֐�":u"�؁[���񂷂�",
	u"CBC���[�h":u"CBC���[��",
	u"CTR���[�h":u"CTR���[�h",
	u"GCM":u"GCM",
	u"POODLE":u"POODLE",
	u"SSL":u"SSL",
	u"TLS":u"TLS",
	u"LSSS":u"LSSS",
	u"AEAD":u"AEAD",
	u"�t�B���K�[�v�����g":u"�ӂ��񂪁[�Ղ���",

	u"CRYPTREC":u"CRYPTREC",
	u"NSA":u"NSA",
	u"���q":u"����",
	u"���K��":u"��������",
	u"Miller�̃A���S���Y��":u"Miller�̂��邲�肸��",

	u"DH���":u"DH���񂾂�",
	u"DLIN����":u"DLIN���Ă�",
	u"BDH���":u"BDH���񂾂�",
	u"CDH���":u"CDH���񂾂�",
	u"DDH���":u"DDH���񂾂�",
	u"SDH���":u"SDH���񂾂�",
	u"BDHE���":u"BDHE���񂾂�",
	u"BDHI���":u"BDHI���񂾂�",
	u"CBDH���":u"CBDH���񂾂�",
	u"DBDH���":u"DBDH���񂾂�",
	u"IND-CCA2":u"IND-CCA2",
	u"MT":u"MT",
	u"Mersenne Twister":u"Mersenne Twister",

	u"FE":u"FE",
	u"SHE":u"SHE",
	u"LWE":u"LWE",
	u"��ݍ���":u"�����݂���",
	u"�Ώ̃y�A�����O":u"�������傤�؂����",
	u"��Ώ̃y�A�����O":u"�Ђ������傤�؂����",
	u"�o���`�ʑ�":u"�������񂯂����Ⴜ��",
	u"�O���铽��":u"����ۂ��ЂƂ�����",
	u"PFS":u"PFS",

	u"DLP":u"DLP",
	u"DSA":u"DSA",
	u"ECDLP":u"ECDLP",
	u"ECDSA":u"ECDSA",
	u"ECDH":u"ECDH",
	u"�ȉ~DH":u"������DH",
	u"EdDSA":u"EdDSA",
	u"IND-CPA":u"IND-CPA",
	u"IND-CCA":u"IND-CCA",
	u"�I�𕽕��U��":u"���񂽂��Ђ�Ԃ񂱂�����",
	u"�I���Í����U��":u"���񂽂����񂲂��Ԃ񂱂�����",
	u"�T�C�h�`���l���U��":u"�����ǂ���˂邱������",
	u"���铽��":u"���傤�ЂƂ�����",
	u"��W��":u"�ЂĂ񂹂�",
	u"���ʕs�\��":u"�����ׂӂ��̂�����",
	u"MAC�l":u"MAC��",
	u"PKI":u"PKI",
	u"PSI":u"PSI",
	u"PFS":u"PFS",
	u"RSA����":u"RSA���Ă�",
	u"�u���C���h����":u"�Ԃ炢��ǂ���߂�",
	u"FDH":u"FDH",
	u"Vernam�Í�":u"Vernam���񂲂�",
	u"distortion�ʑ�":u"distortion���Ⴜ��",

	u"����":u"��񂷂�",
	u"�Í����_�I�[������":u"���񂲂�����Ă�������񂷂�",
	u"�g�[���X":u"�Ɓ[�炷",
	u"���Q":u"�����񂮂�",
	u"�����@��":u"����������",
	u"�����_���E�H�[�N�֐�":u"��񂾂ނ����[�����񂷂�",
	u"����Q":u"����񂩂�����",
	u"������":u"������������",
	u"���n��":u"���񂵂���",
	u"�P�ʌ�":u"���񂢂���",
	u"���ԎҍU��":u"���イ���񂵂Ⴑ������",
	u"MITM":u"MITM",
	u"�p�f�B���O�I���N���U��":u"�ςł��񂮂��炭�邱������",
	u"�o�C�i���@":u"�΂��Ȃ�ق�",
	u"�^�C�������[�X�Í�":u"�����ނ��[�����񂲂�",
	u"�r���_���a":u"�͂��������",
	u"���U�ΐ����":u"�肳�񂽂��������񂾂�",
	u"�閧���U":u"�Ђ݂Ԃ񂳂�",
	u"��񗝘_�I���S":u"���傤�ق�����Ă����񂺂�",
	u"�v�Z�ʓI���S":u"���������傤�Ă����񂺂�",
	u"�����x�[�X�Í�":u"���������ׁ[�����񂲂�",
	u"�[���m���ؖ�":u"���낿�������傤�߂�",
	u"�㗝�Í�":u"�����肠�񂲂�",
	u"�ĈÍ���":u"�������񂲂���",
	u"�F�ؕt���Í�":u"�ɂ񂵂傤�����񂲂�",
	u"PRE":u"PRE",
	u"ID�x�[�X�Í�":u"ID�ׁ[�����񂲂�",
	u"���q":u"����",
	u"��_":u"�ꂢ�Ă�",
	u"�ʐ�":u"������",
	u"�����U��":u"����������������",
	u"�g���":u"������������",
	u"�f��":u"������",
	u"��]��":u"���傤�悩��",
	u"������":u"������������",
	u"���񑽍���":u"���₭����������",
	u"���f����":u"�ӂ�����������",
	u"�W��":u"�Ђ傤����",
	u"Euclid�̌ݏ��@":u"Euclid�̂�����ق�",
	u"�n�b�V���֐�":u"�͂����ォ�񂷂�",
	u"�f�W�^������":u"�ł����邵��߂�",
	u"�L���U��":u"���񂿂傤��������",
	u"SHA-1":u"SHA-1",
	u"SHA-2":u"SHA-2",
	u"SHA-3":u"SHA-3",
	u"�X�|���W":u"���ۂ�",
	u"���k�֐�":u"�������キ���񂷂�",

	u"�~�b�N�X�l�b�g":u"�݂������˂���",
	u"�ĈÍ���":u"�������񂲂���",

	u"�ˉe���":u"���Ⴆ����������",
	u"�ˉe���W":u"���Ⴆ�����Ђ傤",
	u"�A�t�B��":u"���ӂ���",
	u"�Ď�������":u"����������������",
	u"DPVS":u"DPVS",
	u"attribute-hiding":u"attribute-hiding",
	u"payload-hiding":u"payload-hiding",
	u"private-index":u"private-index",
	u"public-index":u"public-index",
	u"bootstrap":u"bootstrap",
	u"���d���`�ʑ�":u"�����イ���񂯂����Ⴜ��",
	u"���ψÍ�":u"�Ȃ��������񂲂�",
	u"�֐��^�Í�":u"���񂷂��������񂲂�",
	u"�q��Í�":u"��������񂲂�",
	u"�����^�C���p�b�h":u"��񂽂��ނς���",

	u"Lagrange���":u"Lagrange�ق���",
	u"Liouville�̒藝":u"Liouville�̂Ă���",
	u"�㐔�I��":u"���������Ă��ւ��ق�",
	u"�㐔�w�̊�{�藝":u"�������������̂��ق�Ă���",
	u"�L���_":u"�䂤��Ă�",
	u"�����_":u"�Ƃ��Ԃ�Ă�",
	u"�˂���_":u"�˂���Ă�",
	u"�Ǐ����W":u"���傭���傴�Ђ傤",
	u"�񍀌W��":u"�ɂ�����������",
	u"�񍀉��Z":u"�ɂ������񂴂�",
	u"�񍀒藝":u"�ɂ����Ă���",
	u"Pascal�̎O�p�`":u"Pascal�̂��񂩂�����",
	u"�|���V�[":u"�ۂ肵�[",
	u"���`�閧���U�@":u"���񂯂��Ђ݂Ԃ񂳂�ق�",
	u"CP-ABE":u"CP-ABE",
	u"KE-ABE":u"KP-ABE",
	u"�r��":u"�͂�����",
	u"�s���Ғǐ�":u"�ӂ������������",
	u"�����֐�":u"���イ�����񂷂�",
	u"���ʎ�":u"�͂�ׂ���",
	u"���^�ʑ�":u"�ǂ��������Ⴜ��",
	u"�Ď����W":u"���������Ђ傤",
	u"Edwards�Ȑ�":u"Edwards���傭����",
	u"DVPS":u"DVPS",
	u"���ݓI�U������":u"���񂴂��Ă�����������Ȃ�",
	u"���S�����^�Í�":u"���񂺂񂶂��ǂ��������񂲂�",
	u"�����":u"���傤���񂵂�",
	u"�F�؋�":u"�ɂ񂵂傤���傭",
	u"���J���ؖ���":u"���������������傤�߂�����",
	u"�������x�N�g��":u"���傫���ׂ��Ƃ�",
	u"�[���m����":u"���낿��������",
	u"���S��":u"���񂺂񂹂�",
	u"���S��":u"���񂺂񂹂�",
	u"�^�����ٓ_":u"���񂹂��Ƃ����Ă�",
	u"�������":u"�����ق���������",
	u"���[�g�ؖ���":u"��[�Ƃ��傤�߂�����",
#	u"��":u"���傭",
#	u"Lagrange�W��":u"Lagrange��������",
#	u"Vandermonde�s��":u"Vandermonde���傤���",
#	$\rho$�@
}

def addIndex(inFile):
	if not inFile.endswith('tex'):
		return
	outFile = '_' + inFile
	fi = codecs.open(inFile, 'r', encoding = 'cp932')
	s = fi.read()
	fi.close()

	for (word, furigana) in wordTbl.items():
		r = u'%s\index{%s@%s}' % (word, furigana, word)
		s = re.sub('([^a-zA-Z{])' + word, '\\1' + r, s)
	s = s.replace(u'�B', u'�D')
	s = s.replace(u'�A', u'�C')

	fo = codecs.open(outFile, 'w', encoding = 'cp932')
	fo.write(s)
	fo.close()

def main():
	if len(sys.argv) != 2:
		print "usage: add_idx.py input.tex"
	addIndex(sys.argv[1])

if __name__ == '__main__':
	main()
