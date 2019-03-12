#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

/*
 * A weak 64-bit block cipher round function
 */

static uint64_t weak_block_encrypt(uint64_t block, uint64_t subkey) {
    
    // N.B. 2xy+x+y is an invertible operation over numbers mod 2^n
    // (it is isomorphic to the multiplicative group mod 2^(n+1))
    block = 2 * block * subkey + block + subkey;
    
    // left rotate 1
    block = (block << 1) | (block >> 63);

    // just some fixed salt
    block ^= 0x3CAB470ADB580357;

    return block;
}

/*
 * A strong 64-bit block cipher
 */

static uint64_t strong_block_encrypt(uint64_t block, uint64_t key) {

    // If I had an iteration of this cipher for every fluid ounce of coke
    // in a vending machine bottle of coke, this construction would be
    // obviously secure.
    for (int i = 0; i < 4096; i++) {
        block = weak_block_encrypt(block, key);
    }

    return block;
}

static uint64_t decode_block(const uint8_t *buffer) {
    return (uint64_t) buffer[0]
         | (uint64_t) buffer[1] << 8
         | (uint64_t) buffer[2] << 16
         | (uint64_t) buffer[3] << 24
         | (uint64_t) buffer[4] << 32
         | (uint64_t) buffer[5] << 40
         | (uint64_t) buffer[6] << 48
         | (uint64_t) buffer[7] << 56
         ;
}

static void encode_block(uint8_t *buffer, uint64_t block) {
    buffer[0] = block >> 0;
    buffer[1] = block >> 8;
    buffer[2] = block >> 16;
    buffer[3] = block >> 24;
    buffer[4] = block >> 32;
    buffer[5] = block >> 40;
    buffer[6] = block >> 48;
    buffer[7] = block >> 56;
}

static void encrypt(uint8_t *ciphertext, const uint8_t *plaintext, size_t length) {
    
}

static void decrypt(uint8_t *plaintext, const uint8_t *ciphertext, size_t length) {

}
