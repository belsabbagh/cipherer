<script>
  export let key;
</script>

<input
  type="number"
  bind:value={key}
  min="1"
  max="25"
  placeholder="Enter key"
/>
