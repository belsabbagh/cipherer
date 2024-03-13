<script>
  import { det } from "mathjs";
  import { modInverse } from "../core/matmath";
  export let key;
  let error = "";
 

  function guardMatrix(matrix) {
    const determinant = det(matrix);
    if (determinant === 0) {
      throw new Error("Invalid key. Matrix is not invertible.");
    }
    if (!matrix.every((row) => row.every((num) => Number.isInteger(num)))) {
      throw new Error("Invalid key. Matrix must contain integers.");
    }
    const detInverse = modInverse(determinant, 26);
    if (detInverse === null) {
      throw new Error("Invalid key. Matrix is not invertible.");
    }
    return true;
  }

  $: {
    try {
      guardMatrix(key);
      error = "";
    } catch (e) {
      error = e;
    }
  }
</script>

<div class="matrix-input">
  {#each key as row, rowIndex}
    <div class="row" id={`${rowIndex}`}>
      {#each row as _, colIndex}
        <input type="number" bind:value={key[rowIndex][colIndex]} />
      {/each}
    </div>
  {/each}
</div>
<div id="error">{error}</div>

<style>
  .matrix-input {
    display: flex;
    flex-direction: column;
  }

  .row {
    display: flex;
  }

  .row input {
    width: 40px;
    margin-right: 5px;
  }

  #error {
    color: rgb(255, 111, 111);
  }
</style>
