We have captured an encrypted message and we need your help to decrypt it! We believe it may give us information as to what started this mess!

Here is the message, it is encrypted using AES-CBC and is base64-encoded:

`uRew7ow7HvGH1UF06hEiMqMENgH8A2HLpZbczI0TAFlRv87LI3F1GrBVwExYvcdykYD2laxRsDToBFrFtjp2vw==`

Through some other information gathering, we found out that whoever sent this message also likes using the following injection vector:

`WHAT_IN_THE_BOOM`

You can use the following connection to test if a message encrypted with the same key and injection vector is correctly padded. We are told that there is an attack vector that you can use to find the message with that information. It accepts messages in base64. Please help us! We must find this information!

`nc pwn.sunshinectf.org 40002`

Author: vraelvrangr
