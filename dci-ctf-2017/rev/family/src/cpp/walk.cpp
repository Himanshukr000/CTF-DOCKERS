unsigned char add(unsigned char n, unsigned char value)
{
    return n + value;
}

unsigned char sub(unsigned char n, unsigned char value)
{
    return n - value;
}

unsigned char xorval(unsigned char n, unsigned char value)
{
    return n ^ value;
}

unsigned char func0(unsigned char n, unsigned char unused)
{
     n = sub(n, 241);
     n = xorval(n, 132);
     n = add(n, 75);
     n = add(n, 22);
     n = add(n, 1);
     n = sub(n, 219);
     n = sub(n, 125);
     n = add(n, 110);
     n = add(n, 149);
     n = add(n, 171);
     n = sub(n, 230);
     n = sub(n, 162);
     n = sub(n, 41);
     n = sub(n, 132);
     return n;
}

unsigned char func1(unsigned char n, unsigned char unused)
{
     n = sub(n, 205);
     n = add(n, 183);
     n = xorval(n, 192);
     n = add(n, 25);
     n = sub(n, 214);
     return n;
}

unsigned char func2(unsigned char n, unsigned char unused)
{
     n = xorval(n, 132);
     n = add(n, 17);
     n = add(n, 211);
     n = xorval(n, 120);
     n = xorval(n, 194);
     n = xorval(n, 243);
     return n;
}

unsigned char func3(unsigned char n, unsigned char unused)
{
     n = xorval(n, 149);
     n = sub(n, 27);
     n = func1(n, 157);
     n = sub(n, 106);
     n = add(n, 25);
     n = func0(n, 56);
     n = func2(n, 225);
     n = func2(n, 106);
     n = func0(n, 214);
     n = sub(n, 59);
     n = sub(n, 14);
     n = add(n, 10);
     n = xorval(n, 180);
     return n;
}

unsigned char func4(unsigned char n, unsigned char unused)
{
     n = add(n, 216);
     n = add(n, 248);
     n = func1(n, 252);
     n = add(n, 229);
     n = func2(n, 174);
     n = add(n, 10);
     n = func1(n, 220);
     n = func3(n, 81);
     n = add(n, 12);
     n = func3(n, 32);
     n = func0(n, 121);
     n = func1(n, 254);
     return n;
}

unsigned char func5(unsigned char n, unsigned char unused)
{
     n = func0(n, 59);
     n = xorval(n, 185);
     n = func4(n, 46);
     n = sub(n, 199);
     n = func1(n, 1);
     n = sub(n, 144);
     n = xorval(n, 118);
     return n;
}

unsigned char func6(unsigned char n, unsigned char unused)
{
     n = func0(n, 57);
     n = func4(n, 217);
     n = xorval(n, 103);
     n = sub(n, 202);
     n = func4(n, 204);
     n = func4(n, 55);
     return n;
}

unsigned char func7(unsigned char n, unsigned char unused)
{
     n = sub(n, 53);
     n = func6(n, 51);
     n = func5(n, 176);
     n = func5(n, 96);
     n = func5(n, 246);
     n = sub(n, 114);
     n = sub(n, 185);
     n = sub(n, 10);
     n = func6(n, 52);
     n = xorval(n, 104);
     return n;
}

unsigned char func8(unsigned char n, unsigned char unused)
{
     n = func2(n, 125);
     n = func5(n, 205);
     n = func4(n, 74);
     n = func2(n, 50);
     n = func0(n, 223);
     n = func1(n, 182);
     n = func1(n, 109);
     n = func6(n, 133);
     return n;
}

unsigned char func9(unsigned char n, unsigned char unused)
{
     n = func4(n, 99);
     n = func0(n, 174);
     n = func6(n, 71);
     n = func8(n, 216);
     n = func6(n, 151);
     n = func5(n, 27);
     n = func8(n, 124);
     n = func4(n, 125);
     n = func7(n, 140);
     n = func2(n, 156);
     return n;
}

unsigned char func10(unsigned char n, unsigned char unused)
{
     n = func1(n, 29);
     n = func6(n, 49);
     n = func5(n, 219);
     n = func5(n, 251);
     n = func3(n, 248);
     n = func1(n, 195);
     n = add(n, 48);
     n = func6(n, 142);
     n = func4(n, 113);
     n = func8(n, 47);
     n = func6(n, 251);
     n = func5(n, 249);
     n = func5(n, 171);
     return n;
}

unsigned char func11(unsigned char n, unsigned char unused)
{
     n = func1(n, 112);
     n = func7(n, 109);
     n = func7(n, 6);
     n = func0(n, 153);
     n = add(n, 78);
     n = func3(n, 213);
     n = func7(n, 48);
     n = func8(n, 113);
     n = func10(n, 135);
     return n;
}

unsigned char func12(unsigned char n, unsigned char unused)
{
     n = sub(n, 31);
     n = func5(n, 229);
     n = func6(n, 248);
     n = sub(n, 125);
     n = func3(n, 154);
     n = func11(n, 61);
     n = func1(n, 153);
     n = func7(n, 78);
     n = xorval(n, 44);
     n = func7(n, 154);
     return n;
}

unsigned char func13(unsigned char n, unsigned char unused)
{
     n = func12(n, 210);
     n = func8(n, 189);
     n = xorval(n, 50);
     n = func11(n, 122);
     n = func6(n, 55);
     n = add(n, 217);
     n = xorval(n, 101);
     n = func4(n, 170);
     n = func3(n, 164);
     n = func8(n, 224);
     n = func10(n, 217);
     return n;
}

unsigned char func14(unsigned char n, unsigned char unused)
{
     n = func9(n, 255);
     n = func4(n, 103);
     n = func2(n, 208);
     n = add(n, 49);
     n = func10(n, 212);
     n = func7(n, 156);
     n = func12(n, 62);
     n = func8(n, 80);
     n = func11(n, 2);
     n = func1(n, 208);
     return n;
}

unsigned char func15(unsigned char n, unsigned char unused)
{
     n = func7(n, 248);
     n = add(n, 124);
     n = func7(n, 249);
     n = func3(n, 105);
     n = func3(n, 30);
     n = func12(n, 209);
     n = func2(n, 54);
     n = func7(n, 254);
     n = func5(n, 45);
     n = func4(n, 12);
     n = func2(n, 122);
     n = func9(n, 119);
     n = func3(n, 51);
     return n;
}

unsigned char func16(unsigned char n, unsigned char unused)
{
     n = add(n, 3);
     n = add(n, 250);
     n = add(n, 55);
     n = func14(n, 181);
     n = func1(n, 82);
     n = func12(n, 61);
     n = func8(n, 48);
     n = xorval(n, 246);
     return n;
}

unsigned char func17(unsigned char n, unsigned char unused)
{
     n = func4(n, 242);
     n = func8(n, 123);
     n = func13(n, 57);
     n = func4(n, 89);
     n = func0(n, 106);
     n = func14(n, 247);
     n = sub(n, 64);
     n = func15(n, 160);
     n = func8(n, 56);
     n = func11(n, 183);
     n = func2(n, 143);
     n = func16(n, 227);
     n = func14(n, 200);
     n = func4(n, 209);
     return n;
}

unsigned char func18(unsigned char n, unsigned char unused)
{
     n = func8(n, 47);
     n = func17(n, 240);
     n = func10(n, 148);
     n = func5(n, 195);
     n = func16(n, 105);
     n = func2(n, 134);
     n = func17(n, 110);
     n = sub(n, 122);
     n = func1(n, 195);
     n = func13(n, 228);
     n = func6(n, 177);
     n = sub(n, 45);
     return n;
}

unsigned char func19(unsigned char n, unsigned char unused)
{
     n = func13(n, 206);
     n = func7(n, 96);
     n = func7(n, 218);
     n = func10(n, 207);
     n = func18(n, 77);
     n = func2(n, 135);
     n = func8(n, 29);
     return n;
}

unsigned char func20(unsigned char n, unsigned char unused)
{
     n = func6(n, 147);
     n = sub(n, 1);
     n = func3(n, 76);
     n = func3(n, 173);
     n = func12(n, 118);
     n = func9(n, 173);
     n = func17(n, 7);
     n = func7(n, 99);
     n = func6(n, 169);
     n = func8(n, 192);
     n = func4(n, 65);
     n = func7(n, 24);
     n = func13(n, 107);
     n = func10(n, 188);
     return n;
}

unsigned char func21(unsigned char n, unsigned char unused)
{
     n = func11(n, 95);
     n = func4(n, 34);
     n = func6(n, 145);
     n = func16(n, 213);
     n = func18(n, 209);
     return n;
}

unsigned char func22(unsigned char n, unsigned char unused)
{
     n = func17(n, 99);
     n = func17(n, 170);
     n = func14(n, 109);
     n = func8(n, 202);
     n = func8(n, 116);
     n = func15(n, 95);
     n = func14(n, 168);
     n = func20(n, 234);
     return n;
}

unsigned char func23(unsigned char n, unsigned char unused)
{
     n = func20(n, 166);
     n = func14(n, 119);
     n = func15(n, 107);
     n = sub(n, 143);
     n = func3(n, 189);
     n = xorval(n, 9);
     return n;
}

unsigned char func24(unsigned char n, unsigned char unused)
{
     n = func3(n, 140);
     n = func4(n, 221);
     n = func19(n, 91);
     n = func15(n, 67);
     n = func4(n, 97);
     n = func14(n, 176);
     n = xorval(n, 109);
     return n;
}

unsigned char func25(unsigned char n, unsigned char unused)
{
     n = func21(n, 88);
     n = func20(n, 33);
     n = func7(n, 71);
     n = func5(n, 4);
     n = func11(n, 50);
     return n;
}

unsigned char func26(unsigned char n, unsigned char unused)
{
     n = func17(n, 239);
     n = func14(n, 183);
     n = func25(n, 66);
     n = func6(n, 110);
     n = add(n, 121);
     n = func13(n, 105);
     n = func15(n, 239);
     n = func11(n, 115);
     return n;
}

unsigned char func27(unsigned char n, unsigned char unused)
{
     n = sub(n, 225);
     n = add(n, 195);
     n = func26(n, 100);
     n = func9(n, 55);
     n = func20(n, 124);
     n = func15(n, 93);
     n = func13(n, 207);
     n = func8(n, 157);
     n = func4(n, 194);
     n = func7(n, 9);
     n = sub(n, 136);
     n = add(n, 126);
     n = func19(n, 146);
     return n;
}

unsigned char func28(unsigned char n, unsigned char unused)
{
     n = func23(n, 92);
     n = func7(n, 225);
     n = func11(n, 142);
     n = func13(n, 170);
     n = func17(n, 62);
     n = func6(n, 255);
     n = func21(n, 11);
     return n;
}

unsigned char func29(unsigned char n, unsigned char unused)
{
     n = func3(n, 185);
     n = func7(n, 81);
     n = func20(n, 210);
     n = func16(n, 113);
     n = func24(n, 24);
     n = func23(n, 4);
     n = func19(n, 76);
     n = func19(n, 208);
     return n;
}

unsigned char walk(unsigned char n, unsigned char unused)
{
     n = add(n, 242);
     n = func10(n, 111);
     n = func6(n, 12);
     n = func3(n, 132);
     n = func15(n, 135);
     n = func29(n, 210);
     n = func15(n, 30);
     n = func18(n, 182);
     n = sub(n, 24);
     n = func4(n, 46);
     n = func17(n, 26);
     n = func18(n, 197);
     n = func14(n, 154);
     n = func13(n, 200);
     n = func8(n, 95);
     n = func24(n, 115);
     n = func27(n, 21);
     n = func29(n, 44);
     n = xorval(n, 43);
     n = func28(n, 245);
     n = func3(n, 195);
     n = xorval(n, 34);
     n = func2(n, 213);
     n = func28(n, 185);
     n = func20(n, 223);
     n = func28(n, 215);
     n = func16(n, 135);
     n = func7(n, 43);
     n = func2(n, 102);
     n = add(n, 7);
     n = func6(n, 139);
     n = func21(n, 23);
     n = add(n, 93);
     n = func7(n, 194);
     n = func24(n, 244);
     n = func16(n, 59);
     n = func3(n, 127);
     n = func16(n, 153);
     n = func10(n, 54);
     n = func10(n, 65);
     n = func16(n, 57);
     n = func6(n, 15);
     n = func26(n, 180);
     n = func4(n, 226);
     n = func6(n, 46);
     n = func11(n, 224);
     n = func28(n, 101);
     n = func20(n, 91);
     n = func21(n, 59);
     n = add(n, 75);
     return n;
}