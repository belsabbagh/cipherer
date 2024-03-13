import * as math from "mathjs";
import { matrixInverseMod26 } from "./matmath";
const alphabet = "abcdefghijklmnopqrstuvwxyz";
const alphabetLength = alphabet.length;

export function make_caesar_cipher() {
  function shift_char(char, shift) {
    const index = alphabet.indexOf(char);
    if (index === -1) {
      return char;
    }
    const newIndex = (index + shift + alphabetLength) % alphabetLength;
    return alphabet[newIndex];
  }

  function encrypt(plaintext, key) {
    return plaintext
      .split("")
      .map((char) => shift_char(char, key))
      .join("");
  }

  function decrypt(ciphertext, key) {
    return ciphertext
      .split("")
      .map((char) => shift_char(char, -key))
      .join("");
  }

  return { encrypt, decrypt };
}

export function make_playfair_cipher() {
  function make_matrix(key) {
    const keySet = new Set(key);
    const keyArray = Array.from(keySet);
    const matrix = keyArray.concat(
      alphabet.split("").filter((char) => !keySet.has(char))
    );
    return matrix;
  }

  function find_char_index(matrix, char) {
    const index = matrix.indexOf(char);
    if (index === -1) {
      throw new Error(`Invalid character: ${char}`);
    }
    return index;
  }

  function find_char_position(matrix, char) {
    const index = find_char_index(matrix, char);
    const row = Math.floor(index / 5);
    const col = index % 5;
    return { row, col };
  }

  function find_char(matrix, row, col) {
    return matrix[row * 5 + col];
  }

  function encrypt_pair(matrix, pair) {
    const { row: row1, col: col1 } = find_char_position(matrix, pair[0]);
    const { row: row2, col: col2 } = find_char_position(matrix, pair[1]);

    if (row1 === row2) {
      return [
        find_char(matrix, row1, (col1 + 1) % 5),
        find_char(matrix, row2, (col2 + 1) % 5),
      ];
    }

    if (col1 === col2) {
      return [
        find_char(matrix, (row1 + 1) % 5, col1),
        find_char(matrix, (row2 + 1) % 5, col2),
      ];
    }

    return [find_char(matrix, row1, col2), find_char(matrix, row2, col1)];
  }

  function decrypt_pair(matrix, pair) {
    const { row: row1, col: col1 } = find_char_position(matrix, pair[0]);
    const { row: row2, col: col2 } = find_char_position(matrix, pair[1]);

    if (row1 === row2) {
      return [
        find_char(matrix, row1, (col1 + 4) % 5),
        find_char(matrix, row2, (col2 + 4) % 5),
      ];
    }

    if (col1 === col2) {
      return [
        find_char(matrix, (row1 + 4) % 5, col1),
        find_char(matrix, (row2 + 4) % 5, col2),
      ];
    }

    return [find_char(matrix, row1, col2), find_char(matrix, row2, col1)];
  }

  function encrypt(plaintext, key) {
    const matrix = make_matrix(key);
    const pairs = plaintext.match(/.{1,2}/g);
    return pairs
      .map((pair) => encrypt_pair(matrix, pair))
      .flat()
      .join("");
  }

  function decrypt(ciphertext, key) {
    const matrix = make_matrix(key);
    const pairs = ciphertext.match(/.{1,2}/g);
    return pairs
      .map((pair) => decrypt_pair(matrix, pair))
      .flat()
      .join("");
  }

  return { encrypt, decrypt };
}

export function make_hill_cipher() {
  function getSubstrings(text, size) {
    const substrings = [];
    for (let i = 0; i < text.length; i += size) {
      substrings.push(text.slice(i, i + size));
    }
    return substrings;
  }

  function matmul(block, key) {
    const result = [];
    for (let i = 0; i < block.length; i++) {
      let sum = 0;
      for (let j = 0; j < block.length; j++) {
        sum += block[j] * key[j][i];
      }
      result.push(sum % 26);
    }
    return result;
  }

  function char2int(char) {
    return char.charCodeAt(0) - 97;
  }

  function int2char(int) {
    return String.fromCharCode(int + 97);
  }

  function process_data(data, matrix) {
    const subs = getSubstrings(data, matrix.length);
    const subVectors = subs.map((block) => Array.from(block, char2int));
    const resVectors = subVectors.map((block) => matmul(block, matrix));
    const resChars = resVectors.map((block) => block.map(int2char).join(""));
    return resChars.join("");
  }



  function encrypt(plaintext, key) {
    const matrix = key;
    return process_data(plaintext, matrix);
  }

  function decrypt(ciphertext, key) {
    const matrix = matrixInverseMod26(key);
    return process_data(ciphertext, matrix);
  }

  return { encrypt, decrypt };
}
export default {
  caesar: make_caesar_cipher(),
  playfair: make_playfair_cipher(),
  hill: make_hill_cipher(),
};
