<template>
    <div>
        <slot></slot>
    </div>
</template>

<script>
  export default {
    name: "status-msg",
    props: {
      type: {
        type: String,
        default: 'success'
      }
    }
  }
</script>

<style scoped>

</style>
