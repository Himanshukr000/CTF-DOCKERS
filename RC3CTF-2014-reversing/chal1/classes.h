// Version: $Id: classes.h,v 1.1 2014/09/29 03:51:19 csci243 Exp $
//
// Defines names for character classes used in the
// CSCI-243 transition matrix project.
//
// @author wrc: Warren R. Carithers

#ifndef _CLASSES_H_
#define _CLASSES_H_

   // whitespace characters:  space, tab
#define	CC_WS		0

   // whitespace character:  newline
#define	CC_NEWLINE	1

   // alphabetic (A-Z, a-z) and underscore
#define	CC_ALPHA	2

   // digit character 0
#define	CC_DIG_0	3

   // digit characters 1-7
#define	CC_DIG_1_7	4

   // digit characters 8, 9
#define	CC_DIG_8_9	5

   // division operator
#define	CC_CHAR_SLASH	6

   // multiplicative operator
#define	CC_CHAR_STAR	7

   // other arithmetic operators: +, -, %
#define	CC_ARITH_OP	8

   // any other ASCII character
#define	CC_OTHER	9

   // EOF on input
#define	CC_EOF		10

   // any non-ASCII character
#define	CC_ERROR	11

   // number of character classes
#define	N_CC		12

#endif

// Revisions:
//	$Log: classes.h,v $
//	Revision 1.1  2014/09/29 03:51:19  csci243
//	Initial revision
//
