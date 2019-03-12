/*
 * Copyright (c) 2015, Bubelich Mykola (bubelich.com)
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * Neither the name of the copyright holder nor the names of its contributors
 * may be used to endorse or promote products derived from this software without
 * specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

import java.nio.ByteBuffer;
import java.util.Arrays;

/**
 * Author: Bubelich Mykola
 * Date: 2015-06-01
 *
 * Implementation of jBaseZ85 data encoding/decoding
 *
 * @author Bubelich Mykola (bubelich.com)
 * @link https://github.com/thesimj/jBaseZ85 (github)
 */
@SuppressWarnings("WeakerAccess")
public final class jBaseZ85 {

    private final static char [] _ALPHA = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-:+=^!/*?&<>()[]{}@%$#".toCharArray();

    private final static int [] _RALPHA = {
            68,0,84,83,82,72,0,75,76,70,65,0,63,62,
            69,0,1,2,3,4,5,6,7,8,9,64,0,73,66,74,71,
            81,36,37,38,39,40,41,42,43,44,45,46,47,
            48,49,50,51,52,53,54,55,56,57,58,59,60,61,
            77,0,78,67,0,0,10,11,12,13,14,15,16,17,18,
            19,20,21,22,23,24,25,26,27,28,29,30,31,32,
            33,34,35,79,0,80};

    private final static int _RALSHIFT = 33;


    /**
     * Encode the Byte array into jBaseZ85 format.
     *
     * @param input byte[] Array of byte to encode.
     * @return String The encoded String
     *
     * @throws RuntimeException
     */
    public static String encode(byte [] input) throws RuntimeException{

        // check input len > 0 or null//
        if(input == null || input.length == 0)
            throw new IllegalArgumentException("Input is wrong");

        int length = input.length;
        int index = 0;
        byte [] buff = new byte[4];

        // Use mutable StringBuilder for fast string append //
        StringBuilder sb = new StringBuilder( (input.length * 5/4) + 1);

        while (length >= 4 ) {

            // copy input to buff //
            buff[3] = input[index++];
            buff[2] = input[index++];
            buff[1] = input[index++];
            buff[0] = input[index++];

            // Append result string to StringBuilder
            sb.append(encodeQuarter(buff));

            length -= 4;
        }

        // Padding zone //
        if(length > 0) {

            buff = new byte[length];

            for (int i = length-1; i >= 0; i--)
                buff[i] = input[index++];

            // Append result string to StringBuilder
            sb.append(encodePadding(buff));
        }

        // Return whole string //
        return sb.toString();
    }

    /**
     * Decodes a jBaseZ85 encoded string.
     *
     * @param input byte[] String The encoded jBaseZ85 String.
     * @return byte[] The decoded array of bytes.
     *
     * @throws RuntimeException
     */
    public static byte[] decode(String input) throws RuntimeException{

        // check input len > 0 or null//
        if(input == null || input.length() == 0)
            throw new IllegalArgumentException("Input is wrong");

        int length = input.length();
        int index = 0;

        char[] buff = new char[5];

        ByteBuffer bytebuff = ByteBuffer.allocate( (length * 4/5) );

        while (length >= 5){

            buff[0] = input.charAt(index++);
            buff[1] = input.charAt(index++);
            buff[2] = input.charAt(index++);
            buff[3] = input.charAt(index++);
            buff[4] = input.charAt(index++);

            bytebuff.put(decodeQuarter(buff));

            length -= 5;
        }

        // If last length > 0 Then need padding //
        if(length > 0) {

            // create padding buffer //
            char [] padding = new char[length];

            // copy last input value to padding buffer //
            for (int i = 0; i < length; i++)
                padding[i] = input.charAt(index++);

            // decode padding //
            bytebuff.put(decodePadding(padding));
        }

        bytebuff.flip();

        if(bytebuff.limit() == 0)
            throw new RuntimeException("Output is empty!");

        return Arrays.copyOf(bytebuff.array(),bytebuff.limit());
    }

    private static char[] encodeQuarter(byte[] data){

        long value = (data[0] & 0x00000000000000FFL) |
                ((data[1] & 0x00000000000000FFL) <<  8) |
                ((data[2] & 0x00000000000000FFL) << 16) |
                ((data[3] & 0x00000000000000FFL) << 24);

        char [] out = new char[5];

        out[0] = _ALPHA[ (int)((value / 0x31C84B1L) % 85) ];
        out[1] = _ALPHA[ (int)((value / 0x95EEDL) % 85) ];
        out[2] = _ALPHA[ (int)((value / 0x1C39L) % 85) ];
        out[3] = _ALPHA[ (int)((value / 0x55L) % 85) ];
        out[4] = _ALPHA[ (int)((value) % 85) ];

        return out;
    }

    /**
     * Encode padding scheme
     *
     * @param data byte[] Array of length = 4 of data
     * @return char[] Encoded padding
     */
    private static char[] encodePadding(byte [] data){

        long value = 0;
        int length = (data.length * 5/4) + 1;
        char [] out = new char[length];

        switch (data.length){
            case 3 : value |= (data[2] & 0x00000000000000FFL) << 16;
            case 2 : value |= (data[1] & 0x00000000000000FFL) << 8;
        }

        value |= (data[0] & 0x00000000000000FFL);

        switch (data.length){
            case 3 :
                out[3] = _ALPHA[ (int)((value / 0x95EEDL) % 85) ];
            case 2:
                out[2] = _ALPHA[ (int)((value / 0x1C39L) % 85) ];
        }

        out[1] = _ALPHA[ (int)((value / 0x55L) % 85) ];
        out[0] = _ALPHA[ (int)((value) % 85) ];

        return out;
    }

    private static byte [] decodeQuarter(char [] data){

        long value = 0;

        value += _RALPHA[data[0] - _RALSHIFT] * 0x31C84B1L;
        value += _RALPHA[data[1] - _RALSHIFT] * 0x95EEDL;
        value += _RALPHA[data[2] - _RALSHIFT] * 0x1C39L;
        value += _RALPHA[data[3] - _RALSHIFT] * 0x55L;
        value += _RALPHA[data[4] - _RALSHIFT];

        return new byte[] {
                (byte) (value >>> 24),
                (byte) (value >>> 16),
                (byte) (value >>> 8),
                (byte) (value)
        };

    }

    private static byte [] decodePadding(char [] data){

        long value = 0;
        int length = data.length * 4 / 5;

        switch (data.length){
            case 4 : value += _RALPHA[data[3] - _RALSHIFT] * 0x95EEDL;
            case 3 : value += _RALPHA[data[2] - _RALSHIFT] * 0x1C39L;
            case 2 : value += _RALPHA[data[1] - _RALSHIFT] * 0x55L;
        }

        value += _RALPHA[data[0] - _RALSHIFT];

        byte [] buff = new byte[length];


        for (int i = length - 1; i >= 0; i--) {
            buff[length-i-1] = (byte)(value >>> 8 * i);
        }

        return buff;
    }
}