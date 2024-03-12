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

export default {
  caesar: make_caesar_cipher(),
  playfair: make_playfair_cipher(),
};
