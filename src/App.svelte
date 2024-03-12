<script>
  import { writable } from "svelte/store";
  import CaesarKeyInput from "./lib/CaesarKeyInput.svelte";
  import PlayfairKeyInput from "./lib/PlayfairKeyInput.svelte";
  import ciphers from "./core/ciphers.js";

  let plaintext = "";
  let key = 1;
  let ciphertext = "";
  let selectedCipher = "caesar";

  const options = {
    caesar: {
      name: "Caesar",
      description:
        "Shifts the letters of the message by a certain number of positions.",
      component: CaesarKeyInput,
    },
    playfair: {
      name: "Playfair",
      description:
        "Encrypts pairs of letters in the message using a 5x5 matrix.",
      component: PlayfairKeyInput,
    },
  };

  const cipherComponent = writable(options[selectedCipher].component);

  $: cipherComponent.set(options[selectedCipher].component);
  function encrypt() {
    console.log(key);
    ciphertext = ciphers[selectedCipher].encrypt(plaintext, key);
  }

  function decrypt() {
    plaintext = ciphers[selectedCipher].decrypt(ciphertext, key);
  }
</script>

<main>
  <h1>Cipherer</h1>
  <p>Enter a message, select a cipher, and enter a key to encrypt it.</p>

  <div>
    <textarea bind:value={plaintext} placeholder="Enter message"></textarea>
    <select bind:value={selectedCipher}>
      {#each Object.keys(options) as cipher}
        <option value={cipher}>{options[cipher].name}</option>
      {/each}
    </select>

    <svelte:component this={$cipherComponent} bind:key />

    <button on:click={encrypt}>Encrypt</button>
    <button on:click={decrypt}>Decrypt</button>
    <div>
      <p>Plaintext: {plaintext}</p>
      <p>Ciphertext: {ciphertext}</p>
    </div>
  </div>
</main>

<style>
  main {
    margin: 20px;
    font-family: Arial, sans-serif;
  }

  textarea {
    width: 100%;
    height: 100px;
    resize: vertical;
    margin-bottom: 10px;
  }

  input[type="number"],
  input[type="text"] {
    width: 80px;
  }

  button {
    margin-top: 10px;
  }

  div {
    margin-top: 20px;
  }
</style>
