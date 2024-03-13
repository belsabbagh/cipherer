import * as math from "mathjs";
export function modInverse(a, m) {
  for (let x = 1; x < m; x++) {
    if ((a * x) % m == 1) {
      return x;
    }
  }
  return null;
}

export function matrixInverseMod26(matrix) {
  const det = Math.round(math.det(matrix));
  const detInverse = modInverse(det, 26);
  const adjugate = math
    .inv(matrix)
    .map((row) => row.map((num) => math.round(num * det)));

  const adjugateArray = [];
  for (let i = 0; i < adjugate.length; i++) {
    adjugateArray[i] = [];
    for (let j = 0; j < adjugate[i].length; j++) {
      adjugateArray[i][j] = adjugate[i][j];
    }
  }

  // Round each element in the adjugate matrix
  for (let i = 0; i < adjugateArray.length; i++) {
    for (let j = 0; j < adjugateArray[i].length; j++) {
      adjugateArray[i][j] = Math.round(adjugateArray[i][j]);
    }
  }
  const inverseMod26 = adjugateArray.map((row) =>
    row.map((num) => (num * detInverse) % 26)
  );
  return inverseMod26;
}
